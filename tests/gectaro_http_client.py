from datetime import datetime
import requests


class GectaroHttpClient:
    def __init__(self, base_url, token, project_id='85531', company='19024'):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.project_id = project_id
        self.company = company

    def get_project_resource_requests(self):
        r = self.session.get(f"{self.base_url}/v1/projects/{self.project_id}/resources")
        if r.status_code != 200:
            print(f"Error: {r.status_code}, {r.text}")
        return r

    def post_project_resource(self, data):
        response = self.session.post(f'{self.base_url}/v1/projects/{self.project_id}/resources', json=data)
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
        return response

    def post_project_resource_requests(self, data):
        id_ = self.session.post(f'{self.base_url}/v1/projects/{self.project_id}/resource-requests',
                                json=data)
        return id_

    def get_project_resource_requests_aplication(self, response_id):
        r = self.session.get(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{response_id}")
        if r.status_code != 200:
            print(f"Error: {r.status_code}, {r.text}")
        return r

    def delete_project_resource_requests_aplication(self, response_id):
        r = self.session.delete(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{response_id}")
        if r.status_code != 200:
            print(f"Error: {r.status_code}, {r.text}")
        return r

    def get_project_resource_requests_companis(self):
        c = self.session.get(f"{self.base_url}/v1/companies/{self.company}/resource-requests")
        if c.status_code != 200:
            print(f"Error: {c.status_code}, {c.text}")
        return c
