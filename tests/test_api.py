from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_idempotency():
    payload = {
        'user_id': 'test-user',
        'attributes': {
            'account_age_days': 150,
            'kyc_verified': True,
            'country': 'IN',
            'monthly_volume': 60000
        }
    }

    r1 = client.post('/evaluate', json=payload)
    r2 = client.post('/evaluate', json=payload)

    assert r1.status_code == 200
    assert r2.status_code == 200

    body1 = r1.json()
    body2 = r2.json()

    assert body1['evaluation_id'] == body2['evaluation_id']
    #assert body1['score'] == body2['score']
    assert body1['decision'] == body2['decision']
