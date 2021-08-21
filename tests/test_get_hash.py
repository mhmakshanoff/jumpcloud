import pytest
import requests
import json
import re

@pytest.fixture
# setup to create a password hash prior to performing get request
def hash_id():
    body = {'password': 'angrymonkey'}
    response = requests.post("http://127.0.0.1:8088/hash", data=json.dumps(body), headers={'content-type': 'application/json'})
    yield response.text
    print("teardown")

# id 10
@pytest.mark.critical
def test_get_hash_check_status_code_equals_200(hash_id):
    response = requests.get(f'http://127.0.0.1:8088/hash/{hash_id}')
    assert response.status_code == 200
    regex = re.compile(r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$')
    assert regex.search(response.text) is not None

# id 11 - expected to fail due to bug
@pytest.mark.medium
def test_get_hash_invalid_id_check_status_code_equals_404():
    response = requests.post("http://127.0.0.1:8088/hash/999")
    assert response.status_code == 404

# id 12
@pytest.mark.medium
def test_get_hash_no_id_check_status_code_equals_405():
    response = requests.put("http://127.0.0.1:8088/hash")
    assert response.status_code == 405
