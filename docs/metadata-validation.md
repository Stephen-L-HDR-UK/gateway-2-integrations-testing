## Schema Validation

Once you have created your metadata, for example for the HDRUK schema `2.1.2`, you can use [various routes](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/docs/) of the translation service to check to see if it validates against this schema:

=== "python"

    Using python `requests`
    ``` python

    metadata = json.load(open("example-hdruk212.json"))

    headers = {
        "Content-Type": "application/json",
    }

    traser_uri = "https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app"
    response = requests.post(
        f"{traser_uri}/find?with_errors=1", headers=headers, json=metadata
    )

    print(json.dumps(response.json(), indent=6))

    ```

=== "CURL"

    ```bash
     curl --location 'http://localhost:3001/find?with_errors=1' \
        --header 'Content-Type: application/json' \
        --data-raw '{<data>}'
    ```

Responds with:

```
[
    {
            "name": "HDRUK",
            "version": "2.1.2",
            "matches": true,
            "errors": null
    },
    {
            "name": "HDRUK",
            "version": "2.1.3",
            "matches": false,
            "errors": [
                {
                        "instancePath": "/provenance/temporal",
                        "schemaPath": "#/required",
                        "keyword": "required",
                        "params": {
                            "missingProperty": "publishingFrequency"
                        },
                        "message": "must have required property 'publishingFrequency'"
                },
                {
                        "instancePath": "/provenance",
                        "schemaPath": "#/properties/provenance/anyOf/1/type",
                        "keyword": "type",
                        "params": {
                            "type": "null"
                        },
                        "message": "must be null"
                },
                {
                        "instancePath": "/provenance",
                        "schemaPath": "#/properties/provenance/anyOf",
                        "keyword": "anyOf",
                        "params": {},
                        "message": "must match a schema in anyOf"
                }
            ]
    },
    ....
    {
            "name": "HDRUK",
            "version": "2.2.0",
            "matches": false,
            "errors": [
                {
                        "instancePath": "/summary",
                        "schemaPath": "#/required",
                        "keyword": "required",
                        "params": {
                            "missingProperty": "datasetType"
                        },
                        "message": "must have required property 'datasetType'"
                }
            ]
    },
    {
            "name": "GWDM",
            "version": "1.0",
            "matches": false,
            "errors": [
                {
                        "instancePath": "",
                        "schemaPath": "#/required",
                        "keyword": "required",
                        "params": {
                            "missingProperty": "required"
                        },
                        "message": "must have required property 'required'"
                }
            ]
    },
    ...
    {
            "name": "SchemaOrg",
            "version": "BioSchema",
            "matches": false,
            "errors": [
                {
                        "instancePath": "",
                        "schemaPath": "#/required",
                        "keyword": "required",
                        "params": {
                            "missingProperty": "name"
                        },
                        "message": "must have required property 'name'"
                }
            ]
    },
    ...
]
```

You can use the route `validate` instead of `find` to validate a payload against an expected schema.

=== "python"

    ```python

    metadata = json.load(open("example-hdruk212.json"))

    response = requests.post(
        f"{traser_uri}/validate?input_schema=HDRUK&input_version=2.1.2",
        headers=headers, json={"metadata":metadata}
    )

    print(json.dumps(response.json(), indent=6))
    ```

    Will response with:
    ```
    {
        "details": "all ok"
    }
    ```
    If the metadata validates

    Otherwise you may see errors that give you details of problems, such as:
    ```
    [
      {
            "instancePath": "/provenance/temporal/timeLag",
            "schemaPath": "#/$defs/TimeLag/enum",
            "keyword": "enum",
            "params": {
                  "allowedValues": [
                        "LESS 1 WEEK",
                        "1-2 WEEKS",
                        "2-4 WEEKS",
                        "1-2 MONTHS",
                        "2-6 MONTHS",
                        "MORE 6 MONTHS",
                        "VARIABLE",
                        "NO TIMELAG",
                        "NOT APPLICABLE",
                        "OTHER",
                        null
                  ]
            },
            "message": "must be equal to one of the allowed values"
      },
        ...

    ```

=== "CURL"

    ```
    curl --location 'http://localhost:3001/validate?input_schema=HDRUK&input_version=2.1.2' \
    --header 'Content-Type: application/json' \
    --data-raw '{<data>}'
    ```
