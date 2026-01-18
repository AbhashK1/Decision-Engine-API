"""from app.data.decision_tree import decision_tree

class DecisionEngine:
    def evaluate(self, attributes):
        return decision_tree.evaluate(attributes)"""

from app.core.decision_tree_builder import build_tree
from app.data.decision_tree import decision_tree_data
from app.core.decision_node import DecisionNode

class DecisionEngine:
    def __init__(self):
        self.root: DecisionNode = build_tree(decision_tree_data)

    def evaluate(self, attributes: dict):
        return self.root.evaluate(attributes)

