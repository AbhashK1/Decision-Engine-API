from app.core.safe_eval import evaluate_condition

class RuleEngine:
    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, attributes):
        score = 0.0
        reasons = []
        triggered = []

        for rule in self.rules:
            if evaluate_condition(rule.condition, attributes):
                triggered.append(rule.id)
                reasons.append(rule.reason)

                if rule.hard_reject:
                    return {
                        'decision': 'REJECT',
                        'score': 0.0,
                        'reasons': reasons,
                        'rules_triggered': triggered
                    }

                if rule.weight:
                    score += rule.weight

        decision = 'APPROVE' if score >= 0.5 else 'REVIEW'

        return {
            'decision': decision,
            'score': round(score, 2),
            'reasons': reasons,
            'rules_triggered': triggered
        }
