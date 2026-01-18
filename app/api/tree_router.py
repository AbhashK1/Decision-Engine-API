from fastapi import APIRouter, HTTPException
from datetime import datetime

from app.models.request import EvaluationRequest
from app.models.response import EvaluationResponse
from app.core.decision_engine import DecisionEngine
from app.core.hashing import payload_hash, evaluation_uuid
from app.repository.evaluation_repo import EvaluationRepository

router = APIRouter()

engine = DecisionEngine()
repo = EvaluationRepository()


@router.post('/evaluate', response_model=EvaluationResponse)
def evaluate(req: EvaluationRequest):
    payload = req.model_dump()
    p_hash = payload_hash(payload)

    cached = repo.get_by_hash(p_hash)
    if cached:
        return cached

    try:
        result = engine.evaluate(req.attributes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    eval_id = evaluation_uuid(p_hash)

    response = {
        'decision': result['decision'],
        'score': result.get('score'),
        'reasons': result.get('path', [result.get('reason')]),
        'rules_triggered': result.get('path', []),
        'evaluation_id': eval_id,
        'timestamp': datetime.utcnow().isoformat()
    }

    repo.save(
        evaluation_id=eval_id,
        payload_hash=p_hash,
        decision=response['decision'],
        score=response['score'],
        response=response
    )

    return response
