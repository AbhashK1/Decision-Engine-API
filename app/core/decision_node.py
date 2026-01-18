from typing import Callable, Dict, Optional

class DecisionNode:
    def __init__(
        self,
        condition: Optional[Callable[[Dict], bool]] = None,
        true_branch=None,
        false_branch=None,
        decision: Optional[str] = None,
        reason: Optional[str] = None,
        label: Optional[str] = None 
    ):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.decision = decision
        self.reason = reason
        self.label = label or reason 

    def evaluate(self, data):
        if self.decision:
            return {
                'decision': self.decision,
                'reason': self.reason,
                'path': [self.label] if self.label else []
            }

        if self.condition(data):
            child_result = self.true_branch.evaluate(data)
        else:
            child_result = self.false_branch.evaluate(data)

        path = [self.label] + child_result.get('path', [])
        return {
            **child_result,
            'path': path
        }
