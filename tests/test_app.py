import app

def test_health_status_code():
    client = app.app.test_client()
    rv = client.get("/health")
    assert rv.status_code == 200
