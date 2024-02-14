There are multiple [metadata schemas](https://github.com/HDRUK/schemata-2) that we support:

-   **Recommended:** [HDRUK 2.2.0](https://hdruk.github.io/schemata-2/HDRUK/2.2.0/) - our public facing schema, our manual-onboarding forms are based on this schema
    -   Older supoprted versions:
        -   [HDRUK 2.1.2](https://hdruk.github.io/schemata-2/HDRUK/2.1.2/)
        -   [HDRUK 2.1.0](https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/models/HDRUK/2.1.0/schema.json)
        -   [HDRUK 2.0.2](https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/models/HDRUK/2.0.2/schema.json)
-   **Other Schemas:**
    -   [BioSchema](https://bioschemas.org/) - we can accept data conforming to this schema definiton, it is just a lot more limited
    -   [Gateway Data Model (GWDM 1.1)](https://hdruk.github.io/schemata-2/GWDM/1.1/) - a looser and more extensive model, used to store any metadata that we accept from the gatway

We also support additional schemas, external to HDRUK, such as [BioSchema](https://bioschemas.org/).

When you create your metadata and `POST` it to our APIs, we convert this metadata, via our [translation service](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/docs/) into our Gateway Data Model (GWDM). Example: `HDRUK 2.2.0` &rarr; `GWDM 1.1`

There are several types and versions of schemas that we can accept as input, validate and translate into our GWDM. It is also possible to retrieve your data in various different schemas by requesting the stored data is translated back into a specific example. Example: `GWDM 1.1` &rarr; `BioSchema`.

What what inputs to the APIs and hence schema translations to the GWDM we can accept are dependent on which [translation](https://github.com/HDRUK/traser-mapping-files/blob/master/available.json) we can accept. Translations are using written using the transformation language [JSONata](https://jsonata.org/). You can visit our [translation-files-repo](https://github.com/HDRUK/traser-mapping-files) to see these translation maps, request new translations so your schema can be supported, report bugs in translations, or submit your own translation map.

## Supported Schemas

To find out what schemas we support, you can use our translation service [(TRASER)](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/docs/) to list what models and what versions of the the model we support.

You can visit the repository [https://hdruk.github.io/schemata-2/](https://hdruk.github.io/schemata-2/) to see a summary of our schemas and a change log between different versions.

Schemas are published as [pydantic](https://docs.pydantic.dev/latest/) models that can be found [here](https://github.com/HDRUK/schemata-2/tree/master/hdr_schemata/models). These models are also exported as [json-schema](https://json-schema.org/), for example: [HDRUK/2.2.0/schema.json](https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/models/HDRUK/2.2.0/schema.json).

=== " python"

    ``` python

    import requests
    import json

    traser_uri = "https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app"
    response = requests.get(f"{traser_uri}/list/schemas")

    print(json.dumps(response.json(), indent=6))

    ```
    Returns data
    ```python
    {
        "HDRUK": [
                "2.1.2",
                "2.1.3",
                "2.1.0",
                "2.0.2",
                "2.2.0"
        ],
        "GWDM": [
                "1.0",
                "1.1"
        ],
        "SchemaOrg": [
                "default",
                "BioSchema",
                "GoogleRecommended"
        ]
    }
    ```

=== "CURL"

    ```bash
    curl --location 'https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/schemas'
    ```

    Returns:
    ```bash
    {"HDRUK":["2.1.2","2.1.3","2.1.0","2.0.2","2.2.0"],"GWDM":["1.0","1.1"],"SchemaOrg":["default","BioSchema","GoogleRecommended"]}
    ```

=== "Web Browser"

    [https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/schemas](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/schemas)

## Supported Translations

Our translation service will also allow you to see what available translations there are

=== " python"

    ``` python

    import requests
    import json

    traser_uri = "ttps://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app"
    response = requests.get(f"{traser_uri}/list/templates")

    print(json.dumps(response.json(), indent=6))

    ```
    Returns data
    ```python
    [
        {
                "output_model": "HDRUK",
                "output_version": "2.1.2",
                "input_model": "HDRUK",
                "input_version": "datasetv2"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.1.2",
                "input_model": "HDRUK",
                "input_version": "2.1.3"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.1.2",
                "input_model": "HDRUK",
                "input_version": "2.0.2"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.1.2",
                "input_model": "GWDM",
                "input_version": "1.0"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.1.2",
                "input_model": "GWDM",
                "input_version": "1.1"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.1.3",
                "input_model": "HDRUK",
                "input_version": "2.1.2"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.0",
                "input_model": "HDRUK",
                "input_version": "2.1.2"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.0",
                "input_model": "GWDM",
                "input_version": "1.1"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.0",
                "input_model": "SchemaOrg",
                "input_version": "default"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.1",
                "input_model": "HDRUK",
                "input_version": "2.1.2"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.1",
                "input_model": "GWDM",
                "input_version": "1.0"
        },
        {
                "output_model": "SchemaOrg",
                "output_version": "default",
                "input_model": "HDRUK",
                "input_version": "2.1.2"
        },
        {
                "output_model": "SchemaOrg",
                "output_version": "default",
                "input_model": "GWDM",
                "input_version": "1.1"
        },
        {
                "output_model": "SchemaOrg",
                "output_version": "BioSchema",
                "input_model": "GWDM",
                "input_version": "1.0"
        },
        {
                "output_model": "SchemaOrg",
                "output_version": "GoogleRecommended",
                "input_model": "HDRUK",
                "input_version": "2.1.2"
        },
        {
                "output_model": "SchemaOrg",
                "output_version": "GoogleRecommended",
                "input_model": "GWDM",
                "input_version": "1.0"
        }
    ]

    ```

=== "CURL"

    ```bash
    curl --location 'https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/templates'
    ```

    Returns:
    ```bash
    [{"output_model":"HDRUK","output_version":"2.1.2","input_model":"HDRUK","input_version":"datasetv2"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"HDRUK","input_version":"2.1.3"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"HDRUK","input_version":"2.0.2"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"GWDM","input_version":"1.0"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"GWDM","input_version":"1.1"},{"output_model":"HDRUK","output_version":"2.1.3","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"GWDM","output_version":"1.0","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"GWDM","output_version":"1.0","input_model":"GWDM","input_version":"1.1"},{"output_model":"GWDM","output_version":"1.0","input_model":"SchemaOrg","input_version":"default"},{"output_model":"GWDM","output_version":"1.1","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"GWDM","output_version":"1.1","input_model":"GWDM","input_version":"1.0"},{"output_model":"SchemaOrg","output_version":"default","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"SchemaOrg","output_version":"default","input_model":"GWDM","input_version":"1.1"},{"output_model":"SchemaOrg","output_version":"BioSchema","input_model":"GWDM","input_version":"1.0"},{"output_model":"SchemaOrg","output_version":"GoogleRecommended","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"SchemaOrg","output_version":"GoogleRecommended","input_model":"GWDM","input_version":"1.0"}]
    ```

=== "Web Browser"

    [https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/templates](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/templates)

## HDRUK 2.2.0 Template

You can fill out the following `JSON` template that matches our HDRUK `2.2.0` schema.

For each value in the `JSON` the template indicates the datatype that should/could be filled so that it passes the metadata validation step.

```json

{
      "identifier": Uuidv4[{'maxLength': 36, 'minLength': 36, 'pattern': '^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', 'type': 'string'}] | Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null,
      "version": Semver[{'pattern': '^([0-9]+)\\\\.([0-9]+)\\\\.([0-9]+)$', 'type': 'string'}],
      "revisions": {
            "version": Semver[{'pattern': '^([0-9]+)\\\\.([0-9]+)\\\\.([0-9]+)$', 'type': 'string'}],
            "url": Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null
      },
      "issued": datetime,
      "modified": datetime,
      "summary": {
            "title": OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}],
            "abstract": AbstractText[{'anyOf': [{'maxLength': 500, 'minLength': 5, 'type': 'string'}, {'type': 'null'}]}] | null,
            "publisher": {
                  "identifier": Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null,
                  "name": OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}],
                  "logo": Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null,
                  "description": Description[{'anyOf': [{'maxLength': 10000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
                  "contactPoint": EmailAddress[{'anyOf': [{'format': 'email', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.EmailAddress.EmailAddress]] | null,
                  "memberOf": MemberOf['HUB','ALLIANCE','OTHER','NCS'] | null
            },
            "contactPoint": EmailAddress[{'anyOf': [{'format': 'email', 'type': 'string'}, {'type': 'null'}]}] | null,
            "keywords": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.OneHundredFiftyCharacters.OneHundredFiftyCharacters] | null,
            "alternateIdentifiers": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.ShortDescription.ShortDescription]] | null,
            "doiName": Doi[{'anyOf': [{'pattern': '^10.\\\\d{4,9}/[-._;()/:a-zA-Z0-9]+$', 'type': 'string'}, {'type': 'null'}]}] | null,
            "datasetType": DatasetType[{'anyOf': [{'maxLength': 100, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
            "datasetSubType": DatasetType[{'anyOf': [{'maxLength': 100, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
            "populationSize": int | null
      },
      "documentation": {
            "description": Description[{'anyOf': [{'maxLength': 10000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
            "associatedMedia": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.Url.Url]] | null,
            "isPartOf": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Union[hdr_schemata.definitions.HDRUK.Url.Url, NoneType, hdr_schemata.definitions.HDRUK.OneHundredFiftyCharacters.OneHundredFiftyCharacters, hdr_schemata.definitions.HDRUK.IsPartOfEnum.IsPartOfEnum]] | null
      },
      "coverage": {
            "spatial": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | null,
            "pathway": LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
            "followup": Followup['0 - 6 MONTHS','6 - 12 MONTHS','1 - 10 YEARS','> 10 YEARS','UNKNOWN','CONTINUOUS','OTHER',null] | null,
            "typicalAgeRange": AgeRange[{'anyOf': [{'pattern': 'Not Known|(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])-(150|1[0-4][0-9]|[0-9]|[1-8][0-9]|9[0-9])', 'type': 'string'}, {'type': 'null'}]}] | null,
            "gender": GenderType['Male','Female','Other'],
            "biologicalsamples": BiologicalSampleType['Blood','Other','Urine','Saliva'],
            "psychological": PsychologicalType['Cognitive Function','Mental Health'],
            "physical": PhysicalType['Respiratory','Vision','Hearing','Musculoskeletal','Cardiovascular','Reproductive'],
            "anthropometric": AnthropometricType['Blood Pressure','Hip Circumference','Height','Waist Circumference','Weight'],
            "lifestyle": LifestylesType['Smoking','Dietary Habits','Physical Activity','Alcohol'],
            "socioeconomic": SocioEconomicType['Finances','Family Circumstances','Housing','Education','Marital Status','Occupation','Ethnic Group','Social Support']
      },
      "provenance": {
            "origin": {
                  "purpose": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.Purpose.Purpose] | null,
                  "source": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.Source.Source] | null,
                  "collectionSituation": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.Setting.Setting] | null
            },
            "temporal": {
                  "distributionReleaseDate": date | datetime | null,
                  "startDate": date | datetime | null,
                  "endDate": date | datetime | EndDateEnum['CONTINUOUS',null] | null,
                  "timeLag": TimeLag['LESS 1 WEEK','1-2 WEEKS','2-4 WEEKS','1-2 MONTHS','2-6 MONTHS','MORE 6 MONTHS','VARIABLE','NO TIMELAG','NOT APPLICABLE','OTHER',null],
                  "publishingFrequency": Periodicity['STATIC','IRREGULAR','CONTINUOUS','BIENNIAL','ANNUAL','BIANNUAL','QUARTERLY','BIMONTHLY','MONTHLY','BIWEEKLY','WEEKLY','SEMIWEEKLY','DAILY','OTHER',null]
            }
      },
      "accessibility": {
            "usage": {
                  "dataUseLimitation": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.DataUseLimitation.DataUseLimitation] | null,
                  "dataUseRequirements": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.DataUseRequirements.DataUseRequirements] | null,
                  "resourceCreator": ShortDescription[{'anyOf': [{'maxLength': 1000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.ShortDescription.ShortDescription]] | null,
                  "investigations": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.Url.Url]] | null,
                  "isReferencedBy": Doi[{'anyOf': [{'pattern': '^10.\\\\d{4,9}/[-._;()/:a-zA-Z0-9]+$', 'type': 'string'}, {'type': 'null'}]}] | str | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.Doi.Doi]] | null
            },
            "access": {
                  "accessRights": LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
                  "accessService": LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
                  "accessRequestCost": LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.Url.Url]] | null,
                  "deliveryLeadTime": DeliveryLeadTime['LESS 1 WEEK','1-2 WEEKS','2-4 WEEKS','1-2 MONTHS','2-6 MONTHS','MORE 6 MONTHS','VARIABLE','NOT APPLICABLE','OTHER',null] | null,
                  "jurisdiction": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.Isocountrycode.Isocountrycode] | null,
                  "dataController": LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null,
                  "dataProcessor": LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null
            },
            "formatAndStandards": {
                  "vocabularyEncodingScheme": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.ControlledVocabulary.ControlledVocabulary] | null,
                  "conformsTo": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.StandardisedDataModels.StandardisedDataModels] | null,
                  "language": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.Language.Language] | null,
                  "format": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[hdr_schemata.definitions.HDRUK.Format.Format] | null
            }
      },
      "enrichmentAndLinkage": {
            "qualifiedRelation": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Union[hdr_schemata.definitions.HDRUK.Url.Url, NoneType, hdr_schemata.definitions.HDRUK.OneHundredFiftyCharacters.OneHundredFiftyCharacters]] | null,
            "derivation": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.AbstractText.AbstractText]] | null,
            "tools": CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | typing.List[typing.Optional[hdr_schemata.definitions.HDRUK.Url.Url]] | null
      },
      "observations": [{
            "observedNode": StatisticalPopulationConstrained['PERSONS','EVENTS','FINDINGS'],
            "measuredValue": int,
            "disambiguatingDescription": AbstractText[{'anyOf': [{'maxLength': 500, 'minLength': 5, 'type': 'string'}, {'type': 'null'}]}] | null,
            "observationDate": date | datetime,
            "measuredProperty": MeasuredProperty[{}]
      }],
      "structuralMetadata": [{
            "name": str | null,
            "description": str | null,
            "elements": {
                  "name": Name[{}],
                  "dataType": str,
                  "description": str | null,
                  "sensitive": bool
            }
      }],
      "tissuesSampleCollection": [{
            "dataCategories": TissueDataCategoriesEnum['Biological samples','Survey data','Imaging data','Medical records','National registries','Genealogical records','Physiological/Biochemical measurements','Other'],
            "materialType": MaterialTypeCategories['Blood','DNA','Faeces','Immortalized Cell Lines','Isolated Pathogen','Other','Plasma','RNA','Saliva','Serum','Tissue (Frozen)','Tissue (FFPE)','Urine'],
            "tissueSampleMetadata": {
                  "creationDate": date | datetime | null,
                  "AnatomicalSiteOntologyCode": ICD_0_3[{'anyOf': [{'pattern': '^[C\\\\d]{3}\\\\.\\\\d{4}\\\\/\\\\d{1,4}$', 'type': 'string'}, {'type': 'null'}]}] | null
            },
            "collectionType": TissueCollectionTypeEnum['Case-control','Cohort','Cross-sectional','Longitudinal','Twin-study','Quality control','Population-based','Disease specific','Birth cohort','Other'] | null
      }]
}


```
