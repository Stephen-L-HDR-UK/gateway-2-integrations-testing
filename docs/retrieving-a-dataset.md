The endpoint [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app) can now be used to retrieve your data that you have just `POST` to the HDRUK gateway.

=== " python requests "

    ```python

    response = requests.get(
        f"{api_path}/integrations/datasets/<dataset_id>",
        headers=headers
    )

    print(json.dumps(response.json(), indent=6))
    ```

    Running this returns the dat that we store for your metadata
    ```
     {
        "id": 16,
        "created_at": "2024-02-09T12:10:23.000000Z",
        "updated_at": "2024-02-09T12:10:23.000000Z",
        "deleted_at": null,
        "dataset_id": 16,
        "metadata": {
                "metadata": {
                    "required": {
                            "gatewayId": "16",
                            "gatewayPid": "5537be3a-e448-4214-8946-8ce1e75a74c8",
                            "issued": "2024-02-09T12:10:23.591675Z",
                            "modified": "2024-02-09T12:10:23.591698Z",
                            "revisions": [],
                            "version": "3.0.0"
                    },
                    ...
    ```

=== "CURL"

    <to do>
