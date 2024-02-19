Method `PUT` [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app) you can update your dataset metadata with a new version

=== " python requests "

    ```python

    response = requests.put(
        f"{api_path}/integrations/datasets/",
        headers=headers,
        json={"metadata": metadata},
    )

    ```

=== "CURL"

    ```
    curl -X PUT \
        --location 'https://api.dev.hdruk.cloud/api/v1/integrations/datasets/<dataset_id>' \
        --header 'x-application-id: <your app ID >' \
        --header 'x-client-id: <your client ID >' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "metadata": {<JSON metadata conforming to supported schema>}
        }'
    ```

Running this returns a structure like:

```
{
      "message": "success",
      "data": {
            "id": 875,
            ...
            "create_origin": "API",
            "status": "ACTIVE",
            "versions": [
                  {
                        "id": 875,
                        ...
                  },
                  ...
            ]
      }
}
```

It returns what data we now hold for this dataset (i.e. multiple versions as you have now updated your dataset with a new version)

### Errors

Please see the previous page for dataset creation, the errors you may receive from an update will be similar to errors you can get from creating a dataset - they'll most likely be due to incorrect metadata or non-existing a non-existing dataset.
