The endpoint [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app) can now be used to retrieve your data that you have just `POST` to the HDRUK gateway.

=== " python "

    ```python

    response = requests.get(
        f"{api_path}/integrations/datasets/<dataset_id>",
        headers=headers
    )

    ```

=== "CURL"

    ```
        curl --location 'https://api.dev.hdruk.cloud/api/v1/integrations/datasets/<dataset_id>' \
        --header 'x-application-id: <your app ID >' \
        --header 'x-client-id: <your client ID >'
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

### Alternative metadata schema

You can request to get your dataset metadata back using a different schema model/version, depending on what we have supported (see previous sections on available schemas and translations).

#### BioSchema

=== " python "

    ```python

    response = requests.get(
        f"{api_path}/integrations/datasets/<dataset_id>?schema_model=SchemaOrg&schema_version=BioSchema",
        headers=headers
    )

    ```

=== "CURL"

    ```bash
        curl --location 'https://api.dev.hdruk.cloud/api/v1/integrations/datasets/<dataset_id>?schema_model=SchemaOrg&schema_version=BioSchema' \
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

Using `/api/v1/integrations/datasets/<dataset_id>?schema_model=HDRUK&schema_version=2.2.0`

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
    }
}
```

### Errors

Please find below a summary of likely errors and their meanings.

#### Cannot find dataset by <dataset_id>

If the `<dataset_id>` that you use to retrieve your dataset (`/api/v1/integrations/datasets/<dataset_id>`) does not exist or is invalid then you'll see the following error:

```json
{
    "status": "INVALID_ARGUMENT",
    "message": "Invalid argument(s)",
    "errors": [
        {
            "reason": "EXISTS",
            "message": "The selected id is invalid.",
            "field": "id"
        }
    ]
}
```

If a dataset has been created and then subsquently deleted you will get the following `500` response:

```json
{
      "code": 500,
      "message": "Dataset with id=<dataset_id> cannot be found",
      "details": {...}
}
```

#### Unauthorised permissions to retrieve

If your app did enable permissions to retrieve a dataset then you'll see the following response (code `400`).

```json
{
      "code": 400,
      "message": "Application permissions do not allow this request",
      "details": {...}
}
```

#### No schema version

If you request the data in another model, you must use `/integrations/datasets/{dataset_id}?schema_model={model}&schema_verson={version}"`
otherwise you may get a `500` response if you forgot to specify both:

```json
{
    'code': 500,
    'message': 'You have given a schema_model but not a schema_version',
    ...
}
```

#### Unknown output schema

If you request the output schema that does not exist or is not supported, example `/integrations/datasets/{dataset_id}?schema_model=HDRUK&schema_version=2.2.3`. You'll get the following response and error coming from our translation service. Navigate to 'creating metadata' to learn about what models and translations are supported.

```json
{
    "message": "failed to translate",
    "details": {
        "traser_message": {
            "error": "Translation not found",
            "message": "Request failed with status code 404",
            "details": "Translation for GWDM-1.1 to HDRUK-2.2.3 is not implemented"
        },
        "wasTranslated": false,
        "metadata": null,
        "statusCode": 400
    }
}
```
