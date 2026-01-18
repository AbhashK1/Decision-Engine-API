from pydantic import BaseModel
from typing import List


class EvaluationResponse(BaseModel):
    decision: str
    score: float
    reasons: List[str]
    rules_triggered: List[str]
    evaluation_id: str
    timestamp: str
