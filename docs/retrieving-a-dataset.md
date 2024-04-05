The endpoint [`/api/v1/integrations/datasets/{id}`](https://api.dev.hdruk.cloud/api/documentation#/Datasets/fetch_datasets_integrations) can now be used to retrieve your data that you have just `POST`ed to the HDRUK gateway.

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

Running this returns the data that we store for your metadata

```
{
    "message": "success",
    "data": {
        "id": 16,
        "mongo_object_id": null,
        "mongo_id": null,
        "mongo_pid": null,
        "datasetid": null,
        "pid": "9b76e4c6-a9fc-40e9-9ab3-22c6a93f22c2",
        "source": null,
        "discourse_topic_id": 0,
        "is_cohort_discovery": false,
        "commercial_use": 0,
        "state_id": 0,
        "uploader_id": 0,
        "metadataquality_id": 0,
        "user_id": 5,
        "team_id": 1,
        "views_count": 0,
        "views_prev_count": 0,
        "has_technical_details": 1,
        "created": "2024-04-04 13:29:30",
        "updated": "2024-04-04 13:29:30",
        "submitted": "2024-04-04 13:29:30",
        "published": null,
        "created_at": "2024-04-04T13:29:30.000000Z",
        "updated_at": "2024-04-04T13:29:30.000000Z",
        "deleted_at": null,
        "create_origin": "API",
        "status": "ACTIVE",
        "named_entities": [],
        "collections": [],
        "versions": [
            {
                "id": 662,
                "created_at": "2024-04-04T13:29:30.000000Z",
                "updated_at": "2024-04-04T13:29:30.000000Z",
                "deleted_at": null,
                "dataset_id": 662,
                "metadata": {
                    "metadata": {
                        "required": {
                            "gatewayId": "662",
                            "gatewayPid": "9b76e4c6-a9fc-40e9-9ab3-22c6a93f22c2",
                            "issued": "2024-04-04T13:29:30.039074Z",
                            "modified": "2024-04-04T13:29:30.039087Z",
                            "revisions": [],
                            "version": "3.0.0"
                        },
                        ...
                    }
                }
            },
            ...
        ]
    }
}
```

### Alternative metadata schema

You can request to get your dataset metadata back using a different schema model/version, depending on what we support (see previous sections on available schemas and translations), using the `schema_model` and `scheme_version` query parameters.

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

Sample output:

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

Using `/api/v1/integrations/datasets/<dataset_id>?schema_model=HDRUK&schema_version=2.2.0` you can get back your metadata conforming to our public schema from our Gateway Data Model (GWDM):

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

#### Cannot find dataset by `dataset_id`

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

If your app does not have permissions to retrieve a dataset then you'll see the following response (code `400`):

```json
{
      "code": 400,
      "message": "Application permissions do not allow this request",
      "details": {...}
}
```

#### No schema version

If you request the data in another model, you must supply both `schema_model` and `schema_version`, e.g. `/integrations/datasets/{dataset_id}?schema_model={model}&schema_version={version}"`. Supplying only one will generate the following:

```json
{
    'code': 500,
    'message': 'You have given a schema_model but not a schema_version',
    ...
}
```

#### Unknown output schema

If you request an output schema that does not exist or is not supported, for example `/integrations/datasets/{dataset_id}?schema_model=HDRUK&schema_version=2.2.3`, you will receive the following response and error from the translation service.

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
Navigate within these docs to `Metadata > Create` to learn about what models and translations are supported.
