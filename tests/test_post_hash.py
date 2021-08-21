import pytest
import requests
import json

# id 4
@pytest.mark.critical
def test_post_hash_check_status_code_equals_200():
    body = {'password': 'angrymonkey'}
    response = requests.post("http://127.0.0.1:8088/hash", data=json.dumps(body), headers={'content-type': 'application/json'})
    assert response.status_code == 200

# id 5 - expected to fail due to bug
@pytest.mark.medium
def test_post_hash_response_immediate():
    body = {'password': 'angrymonkey'}
    response = requests.post("http://127.0.0.1:8088/hash", data=json.dumps(body), headers={'content-type': 'application/json'}, timeout=4)

# id 7
@pytest.mark.medium
def test_post_hash_no_password_check_status_code_equals_400():
    response = requests.post("http://127.0.0.1:8088/hash")
    assert response.status_code == 400

# id 8
@pytest.mark.medium
def test_put_hash_check_status_code_equals_405():
    response = requests.put("http://127.0.0.1:8088/hash")
    assert response.status_code == 405

# id 9
@pytest.mark.medium
def test_delete_hash_check_status_code_equals_405():
    response = requests.delete("http://127.0.0.1:8088/hash")
    assert response.status_code == 405
