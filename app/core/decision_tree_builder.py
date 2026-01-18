from typing import Dict
from app.core.decision_node import DecisionNode

def build_tree(node_data: Dict) -> DecisionNode:
    if 'decision' in node_data:
        return DecisionNode(
            decision=node_data['decision'],
            reason=node_data.get('reason'),
            label=node_data.get('label')
        )

    def condition_fn(d):
        return eval(node_data['condition'], {}, {'d': d})

    return DecisionNode(
        condition=condition_fn,
        label=node_data.get('label'),
        true_branch=build_tree(node_data['true_branch']),
        false_branch=build_tree(node_data['false_branch'])
    )
