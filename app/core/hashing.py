import json
import hashlib
import uuid


def payload_hash(payload: dict) -> str:
    normalized = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(normalized.encode()).hexdigest()


def evaluation_uuid(p_hash: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, p_hash))
