from app.core.decision_engine import DecisionEngine


def test_approve_case():
    engine = DecisionEngine()

    attributes = {
        'account_age_days': 200,
        'kyc_verified': True,
        'country': 'IN',
        'monthly_volume': 80000
    }

    result = engine.evaluate(attributes)

    assert result['decision'] == 'APPROVE'
    assert 'KYC verified' in result['path']
    assert 'Allowed country' in result['path']
    assert 'Monthly volume >= 50k' in result['path']


def test_hard_reject_kyc():
    engine = DecisionEngine()

    attributes = {
        'account_age_days': 300,
        'kyc_verified': False,
        'country': 'IN',
        'monthly_volume': 90000
    }

    result = engine.evaluate(attributes)

    assert result['decision'] == 'REJECT'
    assert result['reason'] == 'KYC not verified'
    assert result['path'][-1] == 'KYC not verified'
