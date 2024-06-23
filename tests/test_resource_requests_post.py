import json

from tests.gectaro_http_client import GectaroHttpClient
from datetime import datetime, timedelta

client = GectaroHttpClient("https://api.gectaro.com",
                           token="qO0CTN2o68UblIErYx-OAVvKy2__giB2")


def test_post_resource_requests():
    data = {
        "name": "test_name",
        "needed_at": datetime.now().timestamp(),
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
    response = client.post_project_resource_requests(data=data)
    print(f'Status code: {response.status_code}')
    print(f'Ответ от API: {response.text}')
    response_json = response.json()
    for item in response_json, dict:
        assert item['volume'] is not None
        assert response_json['cost'] == 5
        assert response_json['project_tasks_resource_id'] == resource_id
    assert response.status_code == 201


def test_post_resource_requests_v2():
    data = {
        "name": "test_name",
        "needed_at": datetime.now().timestamp(),
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
    response = client.post_project_resource_requests(data=data)
    print(f'Status code: {response.status_code}')
    print(f'Ответ от API: {response.text}')
    response_json = response.json()
    for item in response_json, dict:
        assert item['id'] is not None
        assert response_json['user_id'] is not None
        assert response_json['batch_parent_request_id'] is None
    assert response.status_code == 201




def test_post_resource_requests_negative():
    data = {
        "name": "test_name",
        "needed_at": datetime.now().timestamp(),
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
            "needed_at": datetime.now().timestamp(),
            "is_over_budget": 1}
    response = client.post_project_resource_requests(data=data)
    print(f'Status code: {response.status_code}')
    print(f'Ответ от API: {response.text}')
    response_json = response.json()
    for item in response_json, dict:
        assert item['id'] is not None
        assert response_json['user_id'] is not None
        assert response_json['batch_parent_request_id'] is None
    assert response.status_code == 422


def test_post_resource_requests_negative_v2():
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
            "volume": -10,
            "cost": -5,
            "needed_at": int(datetime.now().timestamp()),
            "is_over_budget": 1}
    response = client.post_project_resource_requests(data=data)
    print(f'Status code: {response.status_code}')
    print(f'Ответ от API: {response.text}')
    response_json = response.json()
    for item in response_json, dict:
        assert item['volume'] > 0
        assert response_json['user_id'] is not None
        assert response_json['cost'] > 0
        assert response_json['project_tasks_resource_id'] is None
    assert response.status_code == 201
