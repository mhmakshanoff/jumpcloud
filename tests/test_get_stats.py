import pytest
import requests
import json
import ast

@pytest.fixture
# setup to create a password hash prior to performing stats request
def hash_id():
    body = {'password': 'angrymonkey'}
    response = requests.post("http://127.0.0.1:8088/hash", data=json.dumps(body), headers={'content-type': 'application/json'})
    yield response.text
    print("teardown")

# id 13
@pytest.mark.high
def test_get_stats_check_status_code_equals_200(hash_id):
    response = requests.get("http://127.0.0.1:8088/stats")
    assert response.status_code == 200
    dict = ast.literal_eval(response.text)
    assert dict['TotalRequests'] > 0

# id 14 - expected to fail due to bug
@pytest.mark.low
def test_post_stats_check_status_code_equals_405():
    response = requests.post("http://127.0.0.1:8088/stats")
    assert response.status_code == 405

# id 15 - expected to fail due to bug
@pytest.mark.low
def test_put_stats_check_status_code_equals_405():
    response = requests.put("http://127.0.0.1:8088/stats")
    assert response.status_code == 405

# id 16 - expected to fail due to bug
@pytest.mark.low
def test_delete_stats_check_status_code_equals_405():
    response = requests.delete("http://127.0.0.1:8088/stats")
    assert response.status_code == 405
