There are multiple [metadata schemas](https://hdruk.github.io/schemata-2/) that we support that your metadata can conform to and can be submitted to our systems.

!!! tip

    -   **Recommended:** [HDRUK 3.0.0](https://hdruk.github.io/schemata-2/HDRUK/3.0.0/) is our public facing schema. Our manual-onboarding forms are based on this schema.
        -   Older supported versions:
            -   [HDRUK 2.2.1](https://hdruk.github.io/schemata-2/HDRUK/2.2.1/)
            -   [HDRUK 2.1.2](https://hdruk.github.io/schemata-2/HDRUK/2.1.2/)
            -   [HDRUK 2.1.0](https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/models/HDRUK/2.1.0/schema.json)
            -   [HDRUK 2.0.2](https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/models/HDRUK/2.0.2/schema.json)
    -   **Other Schemas:**
        -   [BioSchema](https://bioschemas.org/) - we can accept data conforming to this schema definition, but it is more limited
        -   [Gateway Data Model (GWDM 2.0)](https://hdruk.github.io/schemata-2/GWDM/2.0/) - a more general and flexible model. We use this schema internally to store any metadata that we accept from external sources.

    We also support additional schemas, external to HDRUK, such as [BioSchema](https://bioschemas.org/).

When you create your metadata and `POST` it to our APIs, the [translation service](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/docs/) converts this metadata into the Gateway Data Model (GWDM) for internal storage.

-   Example: `HDRUK 3.0.0` &rarr; `GWDM 2.0`

There are several schemas, each with possibly multiple versions, that we support. Metadata in each can be accepted as input, validated and translated into our GWDM.

It is also possible to retrieve your data in various different schemas by requesting the stored data is translated into a specific schema.

-   Example: `GWDM 1.1` &rarr; `BioSchema`.

The input-output combinations of schemas we support are dependent on the list of [translations](https://github.com/HDRUK/traser-mapping-files/blob/master/available.json) which are implemented. Translations are using written using the transformation language [JSONata](https://jsonata.org/). You can visit our [translation files repo](https://github.com/HDRUK/traser-mapping-files) to see these translation maps; request new translations so your schema can be supported; report bugs in translations; or submit your own translation map.

## Supported Schemas

To find out which schemas we support, you can use our translation service [(TRASER)](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/docs/) to list them, including the specific versions.

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
                "2.2.1",
                "2.2.0",
                "3.0.0"
        ],
        "GWDM": [
                "1.0",
                "1.1",
                "1.2",
                "2.0"
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
    {"HDRUK":["2.1.2","2.1.3","2.1.0","2.0.2","2.2.1","2.2.0","3.0.0"],"GWDM":["1.0","1.1","1.2","2.0"],"SchemaOrg":["default","BioSchema","GoogleRecommended"]}
    ```

=== "Web Browser"

    [https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/schemas](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/schemas)

## Supported Translations

Our translation service will also allow you to see what available translations there are

=== " python"

    ``` python

    import requests
    import json

    traser_uri = "https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app"
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
                "output_version": "3.0.0",
                "input_model": "HDRUK",
                "input_version": "2.2.1"
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
                "output_model": "HDRUK",
                "output_version": "2.2.1",
                "input_model": "HDRUK",
                "input_version": "2.2.0"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.2.1",
                "input_model": "GWDM",
                "input_version": "1.2"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.2.0",
                "input_model": "HDRUK",
                "input_version": "2.1.2"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.2.0",
                "input_model": "HDRUK",
                "input_version": "2.2.1"
        },
        {
                "output_model": "HDRUK",
                "output_version": "2.2.0",
                "input_model": "GWDM",
                "input_version": "1.1"
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
                "input_model": "HDRUK",
                "input_version": "2.2.0"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.1",
                "input_model": "GWDM",
                "input_version": "1.0"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.1",
                "input_model": "GWDM",
                "input_version": "1.2"
        },
        {
                "output_model": "GWDM",
                "output_version": "2.0",
                "input_model": "GWDM",
                "input_version": "1.2"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.1",
                "input_model": "SchemaOrg",
                "input_version": "BioSchema"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.2",
                "input_model": "HDRUK",
                "input_version": "2.2.1"
        },
        {
                "output_model": "GWDM",
                "output_version": "2.0",
                "input_model": "HDRUK",
                "input_version": "3.0.0"
        },
        {
                "output_model": "GWDM",
                "output_version": "1.2",
                "input_model": "GWDM",
                "input_version": "1.1"
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
                "output_version": "BioSchema",
                "input_model": "GWDM",
                "input_version": "1.1"
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
        },
        {
                "output_model": "SchemaOrg",
                "output_version": "GoogleRecommended",
                "input_model": "GWDM",
                "input_version": "2.0"
        }
    ]

    ```

=== "CURL"

    ```bash
    curl --location 'https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/templates'
    ```

    Returns:
    ```bash
    [{"output_model":"HDRUK","output_version":"2.1.2","input_model":"HDRUK","input_version":"datasetv2"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"HDRUK","input_version":"2.1.3"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"HDRUK","input_version":"2.0.2"},{"output_model":"HDRUK","output_version":"3.0.0","input_model":"HDRUK","input_version":"2.2.1"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"GWDM","input_version":"1.0"},{"output_model":"HDRUK","output_version":"2.1.2","input_model":"GWDM","input_version":"1.1"},{"output_model":"HDRUK","output_version":"2.1.3","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"HDRUK","output_version":"2.2.1","input_model":"HDRUK","input_version":"2.2.0"},{"output_model":"HDRUK","output_version":"2.2.1","input_model":"GWDM","input_version":"1.2"},{"output_model":"HDRUK","output_version":"2.2.0","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"HDRUK","output_version":"2.2.0","input_model":"HDRUK","input_version":"2.2.1"},{"output_model":"HDRUK","output_version":"2.2.0","input_model":"GWDM","input_version":"1.1"},{"output_model":"GWDM","output_version":"1.0","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"GWDM","output_version":"1.0","input_model":"GWDM","input_version":"1.1"},{"output_model":"GWDM","output_version":"1.0","input_model":"SchemaOrg","input_version":"default"},{"output_model":"GWDM","output_version":"1.1","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"GWDM","output_version":"1.1","input_model":"HDRUK","input_version":"2.2.0"},{"output_model":"GWDM","output_version":"1.1","input_model":"GWDM","input_version":"1.0"},{"output_model":"GWDM","output_version":"1.1","input_model":"GWDM","input_version":"1.2"},{"output_model":"GWDM","output_version":"2.0","input_model":"GWDM","input_version":"1.2"},{"output_model":"GWDM","output_version":"1.1","input_model":"SchemaOrg","input_version":"BioSchema"},{"output_model":"GWDM","output_version":"1.2","input_model":"HDRUK","input_version":"2.2.1"},{"output_model":"GWDM","output_version":"2.0","input_model":"HDRUK","input_version":"3.0.0"},{"output_model":"GWDM","output_version":"1.2","input_model":"GWDM","input_version":"1.1"},{"output_model":"SchemaOrg","output_version":"default","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"SchemaOrg","output_version":"default","input_model":"GWDM","input_version":"1.1"},{"output_model":"SchemaOrg","output_version":"BioSchema","input_model":"GWDM","input_version":"1.0"},{"output_model":"SchemaOrg","output_version":"BioSchema","input_model":"GWDM","input_version":"1.1"},{"output_model":"SchemaOrg","output_version":"GoogleRecommended","input_model":"HDRUK","input_version":"2.1.2"},{"output_model":"SchemaOrg","output_version":"GoogleRecommended","input_model":"GWDM","input_version":"1.0"},{"output_model":"SchemaOrg","output_version":"GoogleRecommended","input_model":"GWDM","input_version":"2.0"}]
    ```

=== "Web Browser"

    [https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/templates](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app/list/templates)

## HDRUK 3.0.0 Template

You can fill out the following `JSON` template that matches our HDRUK `3.0.0` schema.

For each value in the `JSON` the template indicates the datatype that should/could be filled so that it passes the metadata validation step.

```json

{
      "identifier": "Uuidv4[{'maxLength': 36, 'minLength': 36, 'pattern': '^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', 'type': 'string'}] | Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null",
      "version": "Semver[{'pattern': '^([0-9]+)\\\\.([0-9]+)\\\\.([0-9]+)$', 'type': 'string'}]",
      "revisions": {
            "version": "Semver[{'pattern': '^([0-9]+)\\\\.([0-9]+)\\\\.([0-9]+)$', 'type': 'string'}]",
            "url": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null"
      },
      "issued": "datetime",
      "modified": "datetime",
      "summary": {
            "title": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}]",
            "abstract": "AbstractText[{'anyOf': [{'maxLength': 500, 'minLength': 5, 'type': 'string'}, {'type': 'null'}]}]",
            "dataProvider": {
                  "identifier": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null",
                  "name": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}]",
                  "logo": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null",
                  "description": "Description[{'anyOf': [{'maxLength': 10000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null",
                  "contactPoint": "EmailAddress[{'anyOf': [{'format': 'email', 'type': 'string'}, {'type': 'null'}]}] | List",
                  "memberOf": "MemberOf['HUB','ALLIANCE','OTHER','NCS'] | null"
            },
            "populationSize": "int",
            "keywords": "CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | List | null",
            "doiName": "Doi[{'anyOf': [{'pattern': '^10.\\\\d{4,9}/[-._;()/:a-zA-Z0-9]+$', 'type': 'string'}, {'type': 'null'}]}] | null",
            "contactPoint": "EmailAddress[{'anyOf': [{'format': 'email', 'type': 'string'}, {'type': 'null'}]}]",
            "alternateIdentifiers": "CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | List | null"
      },
      "documentation": {
            "description": "Description[{'anyOf': [{'maxLength': 10000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}]",
            "associatedMedia": "CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | List | null",
            "inPipeline": "Pipeline['Available','Not available'] | null"
      },
      "coverage": {
            "spatial": "CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | List",
            "typicalAgeRangeMin": "int | null",
            "typicalAgeRangeMax": "int | null",
            "datasetCompleteness": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null",
            "materialType": "MaterialTypeCategoriesV2['None/not available','Bone marrow','Cancer cell lines','CDNA/MRNA','Core biopsy','DNA','Entire body organ','Faeces','Immortalized cell lines','Isolated pathogen','MicroRNA','Peripheral blood cells','Plasma','PM Tissue','Primary cells','RNA','Saliva','Serum','Swabs','Tissue','Urine','Whole blood','Availability to be confirmed','Other']",
            "followup": "Followup['0 - 6 MONTHS','6 - 12 MONTHS','1 - 10 YEARS','> 10 YEARS','UNKNOWN','CONTINUOUS','OTHER',null] | null",
            "pathway": "Description[{'anyOf': [{'maxLength': 10000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null",
            "gender": "GenderType['Male','Female','Other']"
      },
      "provenance": {
            "origin": {
                  "purpose": "PurposeV2['Research cohort','Study','Disease registry','Trial','Care','Audit','Administrative','Financial','Statuatory','Other',null]",
                  "datasetType": "DatasetTypeV2['Health and disease','Treatments/Interventions','Measurements/Tests','Imaging types','Imaging area of the body','Omics','Socioeconomic','Lifestyle','Registry','Environment and energy','Information and communication','Politics']",
                  "datasetSubType": "DatasetSubType['Mental health','Cardiovascular','Cancer','Rare diseases','Metabolic and Endocrine','Neurological','Reproductive','Maternity and neonatology','Respiratory','Immunity','Musculoskeletal','Vision','Renal and urogenital','Oral and Gastrointestinal','Cognitive Function','Hearing','Others','Vaccines','Preventive','Therapeutic','Laboratory','Other diagnostics','CT','MRI','PET','X-ray','Ultrasound','Pathology','Head','Chest','Arm','Abdomen','Leg','Proteomics','Transcriptomics','Epigenomics','Metabolomics','Multiomics','Metagenomics','Genomics','Education','Crime and Justice','Ethnicity','Housing ','Labour','Ageing ','Economics','Marital status','Social support','Deprivation','Religion','Occupation','Finances','Family circumstance','Smoking','Physical Activity','Dietary habits','Alcohol','Disease Registry (research)','National Disease Registries and Audits','Births and Deaths','Not applicable'] | null",
                  "source": "SourceV2['EPR','Electronic survey','LIMS','Paper-based','Free text NLP','Machine generated','Other']",
                  "collectionSource": "SettingV2['Cohort, study, trial','Clinic','Primary care - Referrals','Primary care - Clinic','Primary care - Out of hours','Secondary care - Accident and Emergency','Secondary care - Outpatients','Secondary care - In-patients','Secondary care - Ambulance','Secondary care - ICU','Prescribing - Community pharmacy','Prescribing - Hospital','Patient report outcome','Wearables','Local authority','National government','Community','Services','Home','Private','Social care - Health care at home','Social care - Other social data','Census','Other',null]",
                  "imageContrast": "Ternary['Yes','No','Not stated'] | null"
            },
            "temporal": {
                  "publishingFrequency": "PeriodicityV2['Static','Irregular','Continuous','Biennial','Annual','Biannual','Quarterly','Bimonthly','Monthly','Biweekly','Weekly','Twice a week','Daily','Other',null]",
                  "distributionReleaseDate": "date | datetime | null",
                  "startDate": "date | datetime",
                  "endDate": "date | datetime | EndDateEnum['CONTINUOUS',null] | null",
                  "timeLag": "TimeLagV2['Less than 1 week','1-2 weeks','2-4 weeks','1-2 months','2-6 months','6 months plus','Variable','Not applicable','Other']"
            }
      },
      "accessibility": {
            "usage": {
                  "dataUseLimitation": "DataUseLimitationV2['General research use','Genetic studies only','No general methods research','No restriction','Research-specific restrictions','Research use only','No linkage']",
                  "dataUseRequirements": "DataUseRequirementsV2['Collaboration required','Ethics approval required','Geographical restrictions','Institution-specific restrictions','Not for profit use','Project-specific restrictions','Publication moratorium','Publication required','Return to database or resource','Time limit on use','User-specific restriction']",
                  "resourceCreator": "ShortDescription[{'anyOf': [{'maxLength': 1000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | List | null"
            },
            "access": {
                  "accessRights": "LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}]",
                  "accessServiceCategory": "AccessService['TRE/SDE','Direct access','Open access','Varies based on project'] | null",
                  "accessMode": "AccessMode['Join research consortium','New project'] | null",
                  "accessService": "LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null",
                  "accessRequestCost": "LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null",
                  "deliveryLeadTime": "DeliveryLeadTimeV2['Less than 1 week','1-2 weeks','2-4 weeks','1-2 months','2-6 months','More than 6 months','Variable','Not applicable','Other'] | null",
                  "jurisdiction": "CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | List | null",
                  "dataController": "LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null",
                  "dataProcessor": "LongDescription[{'anyOf': [{'maxLength': 50000, 'minLength': 2, 'type': 'string'}, {'type': 'null'}]}] | null"
            },
            "formatAndStandards": {
                  "vocabularyEncodingScheme": "ControlledVocabulary[{'$defs': {'ControlledVocabularyEnum': {'enum': ['LOCAL', 'OPCS4', 'READ', 'SNOMED CT', 'SNOMED RT', 'DM PLUS D', 'DM+D', 'NHS NATIONAL CODES', 'NHS SCOTLAND NATIONAL CODES', 'NHS WALES NATIONAL CODES', 'ODS', 'LOINC', 'ICD10', 'ICD10CM', 'ICD10PCS', 'ICD9CM', 'ICD9', 'ICDO3', 'AMT', 'APC', 'ATC', 'CIEL', 'HPO', 'CPT4', 'DPD', 'DRG', 'HEMONC', 'JMDC', 'KCD7', 'MULTUM', 'NAACCR', 'NDC', 'NDFRT', 'OXMIS', 'RXNORM', 'RXNORM EXTENSION', 'SPL', 'OTHER'], 'title': 'ControlledVocabularyEnum', 'type': 'string'}}, 'anyOf': [{'$ref': '#/$defs/ControlledVocabularyEnum'}, {'type': 'null'}], 'default': null}]",
                  "conformsTo": "StandardisedDataModels[{'$defs': {'StandardisedDataModelsEnum': {'enum': ['HL7 FHIR', 'HL7 V2', 'HL7 CDA', 'HL7 CCOW', 'LOINC', 'DICOM', 'I2B2', 'IHE', 'OMOP', 'OPENEHR', 'SENTINEL', 'PCORNET', 'CDISC', 'NHS DATA DICTIONARY', 'NHS SCOTLAND DATA DICTIONARY', 'NHS WALES DATA DICTIONARY', 'LOCAL', 'OTHER'], 'title': 'StandardisedDataModelsEnum', 'type': 'string'}}, 'anyOf': [{'$ref': '#/$defs/StandardisedDataModelsEnum'}, {'type': 'null'}], 'default': null}]",
                  "language": "CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | List | null",
                  "format": "CommaSeparatedValues[{'anyOf': [{'pattern': '([^,]+)', 'type': 'string'}, {'type': 'null'}]}] | List | null"
            }
      },
      "enrichmentAndLinkage": {
            "derivedFrom": {
                  "pid": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "title": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "url": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null"
            },
            "isPartOf": {
                  "pid": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "title": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "url": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null"
            },
            "linkableDatasets": {
                  "pid": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "title": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "url": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null"
            },
            "similarToDatasets": {
                  "pid": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "title": "OneHundredFiftyCharacters[{'maxLength': 150, 'minLength': 2, 'type': 'string'}] | null",
                  "url": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}] | null"
            },
            "investigations": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}]",
            "tools": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}]",
            "publicationAboutDataset": "Doi[{'anyOf': [{'pattern': '^10.\\\\d{4,9}/[-._;()/:a-zA-Z0-9]+$', 'type': 'string'}, {'type': 'null'}]}]",
            "publicationUsingDataset": "Doi[{'anyOf': [{'pattern': '^10.\\\\d{4,9}/[-._;()/:a-zA-Z0-9]+$', 'type': 'string'}, {'type': 'null'}]}]"
      },
      "observations": {
            "observedNode": "StatisticalPopulationConstrainedV2['Person','Event','Findings','Number of scans per modality']",
            "measuredValue": "int",
            "disambiguatingDescription": "AbstractText[{'anyOf': [{'maxLength': 500, 'minLength': 5, 'type': 'string'}, {'type': 'null'}]}] | null",
            "observationDate": "date | datetime",
            "measuredProperty": "MeasuredProperty[{}]"
      },
      "structuralMetadata": {
            "tables": {
                  "name": "str | null",
                  "description": "str | null",
                  "columns": {
                        "name": "Name[{}]",
                        "dataType": "str",
                        "description": "str | null",
                        "sensitive": "bool",
                        "values": {
                              "name": "Name[{}]",
                              "description": "str | null",
                              "frequency": "int | null"
                        }
                  }
            },
            "syntheticDataWebLink": "Url[{'anyOf': [{'format': 'uri', 'minLength': 1, 'type': 'string'}, {'type': 'null'}]}]"
      }
}


```
