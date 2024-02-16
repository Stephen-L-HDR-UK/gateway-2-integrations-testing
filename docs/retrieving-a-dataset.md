The endpoint [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app) can now be used to retrieve your data that you have just `POST` to the HDRUK gateway.

=== " python "

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

### Alternative metadata schema

You can request to get your dataset metadata back using a different schema model/version, depending on what we have supported (see previous sections on available schemas and translations).

#### BioSchema

=== " python requests "

    ```python

    response = requests.get(
        f"{api_path}/integrations/datasets/<dataset_id>?schema_model=SchemaOrg&schema_version=BioSchema",
        headers=headers
    )

    ```

=== "CURL"

    ```bash
        curl --location 'https://api.dev.hdruk.cloud/api/v1/integrations/datasets/875?schema_model=SchemaOrg&schema_version=BioSchema' \
            --header 'x-application-id: <application id>' \
            --header 'x-client-id: <client id>' \
    ```

Will return the `data` payload with your metadata in your requested model (and version), if it is possible to translated between our GWDM and the output model.

```json

{
    "message": "success, translated to model=SchemaOrg version=BioSchema",
    "data": {
        "@context": "https://schema.org/",
        "@id": "https://hdruk.ac.uk",
        "@type": "Dataset",
        ...
    }
}

```

#### HDRUK 2.2.0 (public schema)

Using `/api/v1/integrations/datasets/875?schema_model=HDRUK&schema_version=2.2.0`

You can get back your metadata conforming to our public schema from our gateway data model (GWDM)

```json
{
    "message": "success, translated to model=HDRUK version=2.2.0",
    "data": {
        "identifier": "96bea284-dd48-4617-84e5-8b8f888b2fb3",
        "issued": "2021-05-10T00:00:00.000Z",
        "modified": "2024-02-16T15:00:55.934192Z",
        "revisions": [
            {
                "url": "https://placeholder.blah/96bea284-dd48-4617-84e5-8b8f888b2fb3?version=3.0.0",
                "version": "3.0.0"
            }
        ],
        "version": "3.0.1",
        ...
```
