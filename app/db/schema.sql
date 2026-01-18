CREATE TABLE IF NOT EXISTS evaluations (
    evaluation_id TEXT PRIMARY KEY,
    payload_hash TEXT UNIQUE NOT NULL,
    decision TEXT NOT NULL,
    score REAL NOT NULL,
    response TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_payload_hash
ON evaluations(payload_hash);
