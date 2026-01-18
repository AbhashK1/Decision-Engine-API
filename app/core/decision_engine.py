from app.data.decision_tree import decision_tree

class DecisionEngine:
    def evaluate(self, attributes):
        return decision_tree.evaluate(attributes)
