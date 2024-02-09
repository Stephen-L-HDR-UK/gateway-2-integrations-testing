The endpoint [`/api/v1/integrations/datasets`](https://api.dev.hdruk.cloud/api/documentation#/Dataset%20Integrations/create_datasets_from_app) should be used to create dataset(s) on the gateway by posting metadata describing these datasets to our API endpoint.

You should POST application/JSON data to the endpoint where your metadata validates against one of [our supported schemas](https://github.com/HDRUK/schemata-2/blob/master/available.json)

```json
{"metadata": <metadata>},
```

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

=== "python locust.io"

    Create/using the file `api-test.py`
    ``` python

    from locust import HttpUser, task, between
    import json


    class BetaTester(HttpUser):
        wait_time = between(5, 9)

        metadata = json.load(open("example-hdruk212.json"))

        client_id = "fScHE7KHejPZb0TLh4vgdJoitfymyGSMLt7oS10e"
        app_id = "3pO6liuh64iYRkTlTEpZrdGGj8IJnTFH5h3l7HAC"
        api_path = "/api/v1"
        headers = {
            "client_id": client_id,
            "app_id": app_id,
            "Content-Type": "application/json",
        }


    class UserCreatingDataset(BetaTester):

        @task
        def create_datasets(self):
            data = { "metadata": self.metadata}

            response = self.client.post(
                f"{self.api_path}/integrations/datasets",
                headers=self.headers,
                json=data,
            )
            if response.status_code != 201:
                print("Error:", response.status_code)
            else:
                print(json.dumps(response.json(), indent=6))
    ```

    Run with:
    ```
    locust -f api-test.py --headless -u 1 -r 1 -t 30 --host http://localhost:8000 UserCreatingDataset
    ```

=== "CURL"

    ```
    curl --location 'http://localhost:8000/api/v1/integrations/datasets' \
        --header 'app_id: 3pO6liuh64iYRkTlTEpZrdGGj8IJnTFH5h3l7HAC' \
        --header 'client_id: fScHE7KHejPZb0TLh4vgdJoitfymyGSMLt7oS10e' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "metadata": {
                "required": {
                    "gatewayId": "1234",
                    "gatewayPid": "5124f2",
                    "issued": "2020-08-05T14:35:59Z",
                    "modified": "2021-01-28T14:15:46Z",
                    "version": "0.6.9",
                    "revisions": [
                        {
                            "version": "1.0.0",
                            "url": "https://d5faf9c6-6c34-46d7-93c4-7706a5436ed9"
                        },
                        {
                            "version": "2.0.0",
                            "url": "https://a7ddefbd-31d9-4703-a738-256e4689f76a"
                        },
                        {
                            "version": "0.0.1",
                            "url": "https://9e798632-442a-427b-8d0e-456f754d28dc"
                        },
                        {
                            "version": "2.1.1",
                            "url": "https://a7ddefbd-31d9-4703-a738-256e4689f76a"
                        }
                    ]
                },
                "summary": {
                    "abstract": "Publications that mention HDR-UK (or any variant thereof) in Acknowledgements or Author Affiliations",
                    "contactPoint": "susheel.varma@hdruk.ac.uk",
                    "keywords": "Preprints,Papers,HDR UK",
                    "controlledKeywords": "",
                    "datasetType": "list of papers",
                    "description": "Publications that mention HDR-UK (or any variant thereof) in Acknowledgements or Author Affiliations\n\nThis will include:\n- Papers\n- COVID-19 Papers\n- COVID-19 Preprint",
                    "doiName": "10.1093/ije/dyx196",
                    "shortTitle": "HDR UK Papers & Preprints",
                    "title": "DEF DATASET",
                    "publisher": {
                        "publisherName": "DEF DATA RESEARCH UK"
                    }
                },
                "coverage": {
                    "pathway": "NOT APPLICABLE",
                    "physicalSampleAvailability": "NOT AVAILABLE",
                    "spatial": "https://www.geonames.org/countries/GB/united-kingdom.html",
                    "followup": "UNKNOWN",
                    "typicalAgeRange": "0-0"
                },
                "provenance": {
                    "origin": {
                        "purpose": "OTHER",
                        "source": "MACHINE GENERATED",
                        "collectionSituation": "OTHER"
                    },
                    "temporal": {
                        "endDate": "2022-04-30",
                        "startDate": "2020-03-31",
                        "timeLag": "NOT APPLICABLE",
                        "accrualPeriodicity": "DAILY",
                        "distributionReleaseDate": "2020-11-27"
                    }
                },
                "accessibility": {
                    "access": {
                        "deliveryLeadTime": "OTHER",
                        "jurisdiction": "GB-ENG",
                        "dataController": "HDR UK",
                        "dataProcessor": "HDR UK",
                        "accessRights": "https://raw.githubusercontent.com/HDRUK/papers/master/LICENSE",
                        "accessService": "https://github.com/HDRUK/papers",
                        "accessRequestCost": "Free"
                    },
                    "usage": {
                        "dataUseLimitation": "GENERAL RESEARCH USE",
                        "dataUseRequirement": "RETURN TO DATABASE OR RESOURCE",
                        "resourceCreator": "HDR UK Science Team"
                    },
                    "formatAndStandards": {
                        "vocabularyEncodingSchemes": "OTHER",
                        "conformsTo": "OTHER",
                        "languages": "en",
                        "formats": "CSV,JSON"
                    }
                },
                "linkage": {
                    "isGeneratedUsing": "something",
                    "dataUses": "dunno",
                    "isReferenceIn": "10.5281/zenodo.326615",
                    "tools": "https://github.com/HDRUK/papers",
                    "datasetLinkage": {
                        "isDerivedFrom": "https://web.www.healthdatagateway.org/dataset/fd8d0743-344a-4758-bb97-f8ad84a37357",
                        "isPartOf": "NOT APPLICABLE",
                        "isMemberOf": "blah",
                        "linkedDatasets": "https://web.www.healthdatagateway.org/dataset/fd8d0743-344a-4758-bb97-f8ad84a37357"
                    },
                    "investigations": "https://github.com/HDRUK/papers"
                },
                "observations": [
                    {
                        "observedNode": "FINDINGS",
                        "measuredValue": 575,
                        "observationDate": "2020-11-27",
                        "measuredProperty": "Count",
                        "disambiguatingDescription": "Number of papers with affiliation and/or acknowledgement to HDR UK"
                    }
                ],
                "structuralMetadata": [
                    {
                        "name": "table1",
                        "description": "this is table 1",
                        "columns": [
                            {
                                "name": "column1",
                                "description": "this is column1",
                                "dataType": "String",
                                "sensitive": false
                            }
                        ]
                    }
                ]
            }
        }'
    ```
