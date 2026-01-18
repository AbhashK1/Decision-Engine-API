from pydantic import BaseModel
from typing import Optional


class Rule(BaseModel):
    id: str
    condition: str
    reason: str
    weight: Optional[float] = None
    hard_reject: bool = False
