from pydantic import BaseModel
from typing import Dict, Any


class EvaluationRequest(BaseModel):
    user_id: str
    attributes: Dict[str, Any]
