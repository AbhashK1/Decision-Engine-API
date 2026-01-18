from fastapi import APIRouter, HTTPException
from app.models.request import EvaluationRequest
from app.models.response import EvaluationResponse
from app.core.rule_engine import RuleEngine
from app.core.hashing import payload_hash, evaluation_uuid
from app.repository.evaluation_repo import EvaluationRepository
from app.data.rules import RULES
from datetime import datetime

router = APIRouter()
engine = RuleEngine(RULES)
repo = EvaluationRepository()


@router.post('/evaluate', response_model=EvaluationResponse)
def evaluate(req: EvaluationRequest):
    payload = req.model_dump()
    p_hash = payload_hash(payload)

    cached = repo.get_by_hash(p_hash)
    if cached:
        return cached

    result = engine.evaluate(req.attributes)

    eval_id = evaluation_uuid(p_hash)
    response = {
        **result,
        'evaluation_id': eval_id,
        'timestamp': datetime.utcnow().isoformat()
    }

    repo.save(
        evaluation_id=eval_id,
        payload_hash=p_hash,
        decision=result['decision'],
        score=result['score'],
        response=response
    )

    return response
