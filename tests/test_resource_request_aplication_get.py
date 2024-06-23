from tests.gectaro_http_client import GectaroHttpClient
from datetime import datetime

client = GectaroHttpClient("https://api.gectaro.com",
                           token="qO0CTN2o68UblIErYx-OAVvKy2__giB2")


def test_get_resouce_aplication():
    data = {
        "name": "test_name",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": 85531,
        "type": 1,
        "volume": 5
    }
    resource_id = client.post_project_resource(data=data)
    response_json = resource_id.json()
    resource_id = response_json.get('id')
    print(f"Resource ID: {resource_id}")
    data = {"project_tasks_resource_id": resource_id,
            "volume": 10,
            "cost": 5,
            "needed_at": int(datetime.now().timestamp()),
            "is_over_budget": 1}
    response_id = client.post_project_resource_requests(data=data)
    resp_json = response_id.json()
    response_id = resp_json.get('id')
    print(f'Ответ от API: {response_id}')
    r = client.get_project_resource_requests_aplication(response_id)
    assert r.status_code == 200
    assert r.json() is not None
    assert r.json().get('volume') is not None
    assert r.json().get('write_off') is None


def test_get_resouce_aplication_v2():
    data = {
        "name": "test_name",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": 85531,
        "type": 1,
        "volume": 5
    }
    resource_id = client.post_project_resource(data=data)
    response_json = resource_id.json()
    resource_id = response_json.get('id')
    print(f"Resource ID: {resource_id}")
    data = {"project_tasks_resource_id": resource_id,
            "volume": 10,
            "cost": 5,
            "needed_at": int(datetime.now().timestamp()),
            "is_over_budget": 1}
    response_id = client.post_project_resource_requests(data=data)
    resp_json = response_id.json()
    response_id = resp_json.get('id')
    print(f'Ответ от API: {response_id}')
    r = client.get_project_resource_requests_aplication(response_id)
    print(r.text)
    assert r.status_code == 200
    assert r.json() is not None
    assert r.json().get('batch_number') is None
    assert r.json().get('valuation_id') is None
    assert r.json().get('user_id') == 22998


def test_get_resouce_aplication_negative():
    data = {
        "name": "test_name",
        "needed_at": datetime.now().timestamp(),
        "project_id": 85531,
        "type": 1,
        "volume": "type"
    }
    resource_id = client.post_project_resource(data=data)
    response_json = resource_id.json()
    resource_id = response_json.get('id')
    print(f"Resource ID: {resource_id}")
    data = {"project_tasks_resource_id": resource_id,
            "volume": 10,
            "cost": 5,
            "needed_at": datetime.now().timestamp(),
            "is_over_budget": 1,
            "batch_number": 1}
    response_id = client.post_project_resource_requests(data=data)
    resp_json = response_id.json()
    response_id = resp_json.get('id')
    print(f'Ответ от API: {response_id}')
    r = client.get_project_resource_requests_aplication(response_id)
    print(r.text)
    assert r.status_code == 200
    assert r.json() is not None
    assert r.json().get('batch_number') is not None
    assert r.json().get('valuation_id') is None
    assert r.json().get('user_id') == 22998


def test_get_resouce_aplication_negative_v2():
    data = {
        "name": "test_name",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": 85531,
        "type": 1,
        "volume": 5
    }
    resource_id = client.post_project_resource(data=data)
    response_json = resource_id.json()
    resource_id = response_json.get('id')
    print(f"Resource ID: {resource_id}")
    data = {"project_tasks_resource_id": resource_id,
            "volume": 'text',
            "cost": 5.0,
            "needed_at": int(datetime.now().timestamp()),
            "is_over_budget": 1}
    response_id = client.post_project_resource_requests(data=data)
    resp_json = response_id.json()
    response_id = resp_json.get('id')
    print(f'Ответ от API: {response_id}')
    r = client.get_project_resource_requests_aplication(response_id)
    print(r.text)
    assert r.status_code == 200
    assert r.json() is not None
    assert r.json().get('batch_number') is None
    assert r.json().get('valuation_id') is None
    assert r.json().get('user_id') == 22998
