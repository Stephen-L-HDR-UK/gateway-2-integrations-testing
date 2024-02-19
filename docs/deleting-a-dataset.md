Deleting an dataset using `DELETE` on the endpoint [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app)
=== " python "

    ```python

    response = requests.delete(
        f"{api_path}/integrations/datasets/<dataset_id>",
        headers=headers
    )


    ```

=== "CURL"

    ```bash
    curl -X DELETE \
            --location 'https://api.dev.hdruk.cloud/api/v1/integrations/datasets/<dataset_id>' \
            --header 'x-application-id: <application id>' \
            --header 'x-client-id: <client id>' \
    ```

Running this returns the message if it was successfull

```
{
    "message": "success"
}
```
