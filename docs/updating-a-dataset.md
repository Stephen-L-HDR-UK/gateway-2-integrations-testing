Method `PUT` [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app) you can update your dataset metadata with a new version

=== " python requests "

    Using python `requests`
    ``` python
    import requests
    import json

    metadata = json.load(open("example-hdruk212.json"))


    client_id = "fScHE7KHejPZb0TLh4vgdJoitfymyGSMLt7oS10e"
    app_id = "3pO6liuh64iYRkTlTEpZrdGGj8IJnTFH5h3l7HAC"
    api_path = "http://localhost:8000/api/v1"
    headers = {
        "client_id": client_id,
        "app_id": app_id,
        "Content-Type": "application/json",
    }


    response = requests.post(
        f"{api_path}/integrations/datasets",
        headers=headers,
        json={"metadata": metadata},
    )

    print(json.dumps(response.json(), indent=6))
    ```

    Running this returns:
    ```
    {
        "message": "created",
        "data": <dataset_id : Integer>,
        "version": <dataset_version: Integer>
    }
    ```

=== "CURL"

   <to do>
