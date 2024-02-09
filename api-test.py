from locust import HttpUser, task, between
import json


class BetaTester(HttpUser):
    wait_time = between(5, 9)

    metadata = json.load(open("example-hdruk212.json"))
    # metadata = json.load(open("example-gwdm10.json"))

    client_id = "fScHE7KHejPZb0TLh4vgdJoitfymyGSMLt7oS10e"
    app_id = "3pO6liuh64iYRkTlTEpZrdGGj8IJnTFH5h3l7HAC"
    api_path = "/api/v1"
    headers = {
        "client_id": client_id,
        "app_id": app_id,
        "Content-Type": "application/json",
    }


class UserCreatingDataset(BetaTester):

    @task
    def create_datasets(self):
        data = {"metadata": self.metadata}

        response = self.client.post(
            f"{self.api_path}/integrations/datasets",
            headers=self.headers,
            json=data,
        )
        print(response.status_code)
        if response.status_code != 201:
            print("Error:", response.status_code)

        print(json.dumps(response.json(), indent=6))
