from app.core.hashing import payload_hash, evaluation_uuid


def test_payload_hash_is_deterministic():
    payload1 = {
        'user_id': 'x',
        'attributes': {'a': 1, 'b': 2}
    }

    payload2 = {
        'attributes': {'b': 2, 'a': 1},
        'user_id': 'x'
    }

    assert payload_hash(payload1) == payload_hash(payload2)


def test_uuid_is_deterministic():
    h = 'test_hash'
    assert evaluation_uuid(h) == evaluation_uuid(h)
