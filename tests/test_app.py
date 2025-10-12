import sys, pathlib

# Ensure the repository root is on sys.path
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app  # now this should succeed

def test_health_status_code():
    client = app.app.test_client()
    rv = client.get("/health")
    assert rv.status_code == 200
