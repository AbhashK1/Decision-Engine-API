from app.core.decision_node import DecisionNode

decision_tree = DecisionNode(
    condition=lambda d: d['kyc_verified'],
    label='KYC verified',
    true_branch=DecisionNode(
        condition=lambda d: d['country'] in ['IN', 'US', 'UK'],
        label='Allowed country',
        true_branch=DecisionNode(
            condition=lambda d: d['account_age_days'] >= 90,
            label='Account age >= 90',
            true_branch=DecisionNode(
                condition=lambda d: d['monthly_volume'] >= 50_000,
                label='Monthly volume >= 50k',
                true_branch=DecisionNode(
                    decision='APPROVE',
                    reason='Strong account with sufficient activity'
                ),
                false_branch=DecisionNode(
                    decision='REVIEW',
                    reason='Low transaction volume'
                )
            ),
            false_branch=DecisionNode(
                decision='REVIEW',
                reason='Account too new'
            )
        ),
        false_branch=DecisionNode(
            decision='REJECT',
            reason='High risk country'
        )
    ),
    false_branch=DecisionNode(
        decision='REJECT',
        reason='KYC not verified'
    )
)
