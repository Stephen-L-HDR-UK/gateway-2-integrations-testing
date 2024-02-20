The endpoint [`/api/v1/integrations/datasets`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app) should be used to create dataset(s) on the gateway by posting metadata describing these datasets to our API endpoint.

You should POST application/JSON data to the endpoint where your metadata validates against one of [our supported schemas](https://github.com/HDRUK/schemata-2/blob/master/available.json)

```json
{"metadata": <metadata>}
```

=== " python "

    Initialise your request client
    ``` python
    import requests
    import json


    client_id = <your client id>
    app_id = <your app id>

    api_path = "https://api.dev.hdruk.cloud/api/v1/"


    headers = {
        "x-client-id": client_id,
        "x-application-id": app_id,
        "Content-Type": "application/json",
    }

    ```

    ```python
    metadata = {"metadata": <JSON metadata conforming to supported schema>}


    response = requests.post(
        f"{api_path}/integrations/datasets",
        headers=headers,
        json=metadata
    )

    print(json.dumps(response.json(), indent=6))
    ```

=== "CURL"

    ```
    curl --location 'https://api.dev.hdruk.cloud/api/v1/integrations/datasets' \
        --header 'x-application-id: <your app ID >' \
        --header 'x-client-id: <your client ID >' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "metadata": {<JSON metadata conforming to supported schema>}
        }'
    ```

Running this returns:

```json
    {
        "message": "created",
        "data": <dataset_id : Integer>,
        "version": <dataset_version_id: Integer>
    }
```

You should make a record of the dataset ID that is returned in the `data` field when the dataset is created. There are various endpoints that you can use to retrieve all your datasets and the IDs for them.

### Errors

Please find below a summary of likely errors and their meanings.

#### Unauthorised permissions to create

If your app did enable permissions to create a dataset then you'll see the following response (code `400`).

```json
{
      "code": 400,
      "message": "Application permissions do not allow this request",
      "details": {...}
}
```

#### No x-application-id or x-client-id in your headers

```json
{
    "code": 401,
    "message": "Please provide a x-application-id and x-client-id in your headers",
    "details": ...
}
```

You need to set these in the headers that you make your requests with. To find the values of these identifiers, navigate (on the gateway) to your integrations API management page (Mange API), click on your App, make sure it is enabled, click on the tab for 'Authentication' to find these values.

#### Invalid App credientials

You've copied your App ID or Client ID wrong when you've added them to the headers

```json
{
    "code": 401,
    "message": "No known integration matches the credentials provided"
    ...
}
```

#### App not enabled

```json
{
    "code": 400,
    "message": "Application has not been enabled!",
    ...
}
```

Navigate (on the gateway) to your integrations API management page (Mange API), click on your App, your the application you have copied over the App and Client ID (from the Authentication tab) make sure the App is set to enabled on the 'App info' tab.
