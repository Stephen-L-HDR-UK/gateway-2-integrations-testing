Deleting an dataset using `DELETE` on the endpoint [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app)
=== " python requests "

    ```python

    response = requests.delete(
        f"{api_path}/integrations/datasets/<dataset_id>",
        headers=headers
    )

    print(json.dumps(response.json(), indent=6))
    ```

    Running this returns the dat that we store for your metadata
    ```
    {
        "message": "success"
    }
    ```

=== "CURL"

    <to do>
