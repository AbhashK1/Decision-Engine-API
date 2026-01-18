from app.models.rule import Rule

RULES = [
    Rule(
        id='RULE_1',
        condition='account_age_days >= 90',
        weight=0.3,
        reason='Account age above threshold'
    ),
    Rule(
        id='RULE_2',
        condition='kyc_verified == False',
        hard_reject=True,
        reason='KYC not verified'
    ),
    Rule(
        id='RULE_3',
        condition="country in ['IN', 'US']",
        weight=0.2,
        reason='Low risk country'
    ),
    Rule(
        id='RULE_4',
        condition='monthly_volume >= 50000',
        weight=0.3,
        reason='Healthy transaction volume'
    )
]
