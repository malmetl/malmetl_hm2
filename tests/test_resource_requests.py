from tests.gectaro_http_client import GectaroHttpClient
from datetime import datetime

client = GectaroHttpClient("https://api.gectaro.com",
                           token="qO0CTN2o68UblIErYx-OAVvKy2__giB2")


def test_get_resources_requests():
    r = client.get_project_resource_requests()
    print(r.status_code)
    print(r.url)
    print(r.json()[1])
    for item in r.json():
        assert item
        assert item["id"] is not None
        assert item["volume"] is not None
    assert r.status_code == 200


def test_get_resources_requests_v2():
    r = client.get_project_resource_requests()
    print(r.status_code)
    print(r.url)
    print(r.json()[0])
    for item in r.json():
        assert item["id"] is not None
        assert item["valuation_id"] is None
        assert item["updated_at"] > 10000
        assert item["cost"] > 0
    assert r.status_code == 200


def test_get_resources_requests_negativ():
    r = client.get_project_resource_requests()
    print(r.status_code)
    print(r.url)
    print(r.json()[1])
    for item in r.json():
        assert item['updated_at'] == 10000
        assert item["id"] is None
        assert item["volume"] == 5
    assert r.status_code == 404


def test_get_resources_requests_negativ_v2():
    r = client.get_project_resource_requests()
    print(r.status_code)
    print(r.url)
    print(r.json()[1])

    for item in r.json():
        assert item['unit_measure_id' == 0]
        assert item["is_in_order"] is None
    assert r.status_code == 404
