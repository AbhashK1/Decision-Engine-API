import sqlite3
import json
from pathlib import Path
from datetime import datetime

DB_PATH = Path('evaluations.db')
SCHEMA_PATH = Path('app/db/schema.sql')


class EvaluationRepository:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        with open(SCHEMA_PATH) as f:
            self.conn.executescript(f.read())
        self.conn.commit()

    def get_by_hash(self, payload_hash: str):
        cur = self.conn.cursor()
        cur.execute(
            'SELECT response FROM evaluations WHERE payload_hash = ?',
            (payload_hash,)
        )
        row = cur.fetchone()
        return json.loads(row[0]) if row else None

    def save(self, evaluation_id, payload_hash, decision, score, response):
        self.conn.execute(
            '''
            INSERT INTO evaluations
            (evaluation_id, payload_hash, decision, score, response, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
                evaluation_id,
                payload_hash,
                decision,
                score,
                json.dumps(response),
                datetime.utcnow().isoformat()
            )
        )
        self.conn.commit()
