from app.core.rule_engine import RuleEngine
from app.data.rules import RULES #app\data\rules.py


def test_approve_case():
    engine = RuleEngine(RULES)

    attributes = {
        'account_age_days': 200,
        'kyc_verified': True,
        'country': 'IN',
        'monthly_volume': 80000
    }

    result = engine.evaluate(attributes)

    assert result['decision'] == 'APPROVE'
    assert result['score'] >= 0.5
    assert 'RULE_2' not in result['rules_triggered']


def test_hard_reject():
    engine = RuleEngine(RULES)

    attributes = {
        'account_age_days': 300,
        'kyc_verified': False,
        'country': 'IN',
        'monthly_volume': 90000
    }

    result = engine.evaluate(attributes)

    assert result['decision'] == 'REJECT'
    assert result['score'] == 0.0
    assert 'RULE_2' in result['rules_triggered']
