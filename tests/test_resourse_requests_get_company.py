from tests.gectaro_http_client import GectaroHttpClient
from datetime import datetime

client = GectaroHttpClient("https://api.gectaro.com",
                           token="qO0CTN2o68UblIErYx-OAVvKy2__giB2")


def test_get_resources_requests():
    r = client.get_project_resource_requests_companis()
    print(r.status_code)
    print(r.url)
    print(r.json()[0])
    for item in r.json():
        assert item
        assert item["id"] is not None
        assert item["volume"] is not None
    assert r.status_code == 200


def test_get_resources_requests_v2():
    r = client.get_project_resource_requests_companis()
    print(r.status_code)
    print(r.url)
    print(r.json()[0])
    for item in r.json():
        assert item
        assert item["project_tasks_resource_id"] is not None
        assert item["batch_number"] is None
        assert item["user_id"] == 22998
    assert r.status_code == 200


def test_get_resources_requests_negative():
    r = client.get_project_resource_requests_companis()
    print(r.status_code)
    print(r.url)
    print(r.json()[0])
    for item in r.json():
        assert item
        assert item["project_tasks_resource_id"] is None
        assert item["batch_number"] is not None
        assert item["user_id"] == 9999999
    assert r.status_code == 200


def test_get_resources_requests_negative_v2():
    r = client.get_project_resource_requests_companis()
    print(r.status_code)
    print(r.url)
    print(r.json()[0])
    for item in r.json():
        assert item
        assert item["volume"] is None
        assert item["batch_parent_request_id"] is not None
        assert item["created_by"] == 9999999
    assert r.status_code == 200
