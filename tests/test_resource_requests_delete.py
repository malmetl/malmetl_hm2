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
    delete_response = client.delete_project_resource_requests_aplication(response_id)
    print(delete_response.url)
    assert delete_response.status_code == 204
    check_response = client.get_project_resource_requests_aplication(response_id)
    assert check_response.status_code == 404


def test_get_resouce_aplication_v2():
    data = {
        "name": "test_name",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": 85531,
        "type": 2,
        "volume": 1235
    }
    resource_id = client.post_project_resource(data=data)
    response_json = resource_id.json()
    resource_id = response_json.get('id')
    print(f"Resource ID: {resource_id}")
    data = {"project_tasks_resource_id": resource_id,
            "volume": 17,
            "cost": 105,
            "needed_at": int(datetime.now().timestamp()),
            "is_over_budget": 1}
    response_id = client.post_project_resource_requests(data=data)
    resp_json = response_id.json()
    response_id = resp_json.get('id')
    print(f'Ответ от API: {response_id}')
    delete_response = client.delete_project_resource_requests_aplication(response_id)
    print(delete_response.url)
    assert delete_response.status_code == 204
    check_response = client.get_project_resource_requests_aplication(response_id)
    assert check_response.status_code == 404


def test_get_resouce_aplication_negative():
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
            "volume": 1230,
            "cost": 5,
            "needed_at": int(datetime.now().timestamp()),
            "is_over_budget": 0}
    response_id = client.post_project_resource_requests(data=data)
    resp_json = response_id.json()
    response_id = resp_json.get('id')
    print(f'Ответ от API: {response_id}')
    delete_response = client.delete_project_resource_requests_aplication(response_id)
    print(delete_response.url)
    assert delete_response.status_code == 204
    check_response = client.get_project_resource_requests_aplication(response_id)
    assert check_response.status_code == 404


def test_get_resouce_aplication_negative_2():
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
            "volume": 1230,
            "cost": 123125,
            "needed_at": int(datetime.now().timestamp()),
            "is_over_budget": 1}
    response_id = client.post_project_resource_requests(data=data)
    resp_json = response_id.json()
    response_id = resp_json.get('id')
    print(f'Ответ от API: {response_id}')
    delete_response = client.delete_project_resource_requests_aplication(response_id)
    print(delete_response.url)
    assert delete_response.status_code == 200
    check_response = client.get_project_resource_requests_aplication(response_id)
    assert check_response.status_code == 404
