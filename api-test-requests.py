import requests
import json


client_id = "fScHE7KHejPZb0TLh4vgdJoitfymyGSMLt7oS10e"
app_id = "3pO6liuh64iYRkTlTEpZrdGGj8IJnTFH5h3l7HAC"
api_path = "http://localhost:8000/api/v1"
headers = {
    "client_id": client_id,
    "app_id": app_id,
    "Content-Type": "application/json",
}

metadata = {"metadata": json.load(open("example-hdruk212.json"))}

# response = requests.post(
#    f"{api_path}/integrations/datasets", headers=headers, json=metadata
# )
# dataset_id = response.json()["data"]

dataset_id = 9

# response = requests.get(
#    f"{api_path}/integrations/datasets/{dataset_id}?schema_model=SchemaOrg&schema_version=BioSchema",
#    headers=headers,
# )

# print(json.dumps(response.json(), indent=6))


response = requests.delete(
    f"{api_path}/integrations/datasets/{dataset_id}", headers=headers
)

print(json.dumps(response.json(), indent=6))
