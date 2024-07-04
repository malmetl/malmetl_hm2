from tests.gectaro_http_client import GectaroHttpClient
from datetime import datetime

client = GectaroHttpClient("https://api.gectaro.com",
                           token="HL4yGX1-3LeTGQbSBsvwFPKceGfzfZsE")


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
    assert r.status_code == 200


def test_get_resources_requests_negative():
    r = client.get_project_resource_requests()
    print(r.status_code)
    print(r.url)
    print(r.json()[1])
    assert r.status_code != 404


def test_get_resources_requests_negativ_v2():
    r = client.get_project_resource_requests()
    print(r.status_code)
    print(r.url)
    print(r.json()[1])
    assert r.status_code != 204
