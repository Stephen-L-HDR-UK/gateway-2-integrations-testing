In this page we provide a few **mock** examples, based on real metadata, publically available on the old version of the HDRUK gateway, that has been modified slightly (e.g. real email addresses and real identifiers) and can be used for examples.

### HDRUK 2.1.2 Schema

Posting the following data (`{"metadata":<json>}`) to the [translation service](https://hdr-gateway-traser-dev-qmnkcg5qjq-ew.a.run.app) endpoint:

`/validate?input_schema=HDRUK&input_version=2.1.2`

will respond with the status code `200` and message:

```json
{
    "details": "all ok"
}
```

??? example "SAIL: Education Daily Attendance Dataset (EDAD)"

    ```json

    {
        "identifier": "https://blah.com/7eb5d9ff-0d54-4438-9c60-423848aebb4c",
        "version": "11.0.0",
        "issued": "2023-08-17T00:00:00.000Z",
        "modified": "2023-08-17T00:00:00.000Z",
        "revisions": [],
        "summary": {
                "title": "Education Daily Attendance Dataset (EDAD)",
                "abstract": "This dataset provides information about daily educational attendance within Wales.",
                "publisher": {
                    "identifier": "https://blah.com/5f3f98068af2ef61552e1d75",
                    "name": "SAIL",
                    "logo": null,
                    "description": null,
                    "contactPoint": null,
                    "memberOf": "ALLIANCE"
                },
                "contactPoint": "SAILDatabank@blah.com",
                "keywords": "Education, SAIL,EDAD,core-res,Health & Wellbeing,Children & Young People,Inequality & Social Inclusion, Housing & Communities",
                "alternateIdentifiers": null,
                "doiName": null
        },
        "documentation": {
                "description": "This dataset provides detailed information about daily educational attendance within Wales.\n\nAttendance data in the EDUW schema was discontinued after 2019 and the Education Daily Attendance Dataset (EDAD) schema replaced it. This dataset contains more detailed information on attendance than was previously available in EDUW.\n\nThere is no ALF within this dataset, projects will need apply for education (EDUW) data to enable ALF linkage to other datasets",
                "associatedMedia": "https://saildatabank.com/about-us/",
                "isPartOf": null
        },
        "coverage": {
                "spatial": "United Kingdom,Wales",
                "typicalAgeRange": "0-20",
                "physicalSampleAvailability": null,
                "followup": "0 - 6 MONTHS",
                "pathway": "Education"
        },
        "provenance": {
                "origin": {
                    "purpose": "ADMINISTRATIVE",
                    "source": "OTHER",
                    "collectionSituation": "OTHER"
                },
                "temporal": {
                    "accrualPeriodicity": "MONTHLY",
                    "distributionReleaseDate": null,
                    "startDate": "2020-09-01",
                    "endDate": "2021-12-17",
                    "timeLag": "2-6 MONTHS"
                }
        },
        "accessibility": {
                "usage": {
                    "dataUseLimitation": "GENERAL RESEARCH USE",
                    "dataUseRequirements": "PROJECT SPECIFIC RESTRICTIONS,USER SPECIFIC RESTRICTION",
                    "resourceCreator": "Welsh Government",
                    "investigations": null,
                    "isReferencedBy": "Littlecott HJ, Moore GF, Moore L, Lyons RA, Murphy S. Association between breakfast consumption and educational outcomes in 9-11-year-old children. Public Health Nutr. 2016 Jun;19(9):1575-82. doi: 10.1017/S1368980015002669. Epub 2015 Sep 28. Erratum in: Public Health Nutr. 2016 Jun;19(9):1583. PMID: 26411331; PMCID: PMC4873891. "
                },
                "access": {
                    "accessRights": "https://saildatabank.com/data/apply-to-work-with-the-data/",
                    "accessService": "The SAIL Databank is powered by the UK Secure e-Research Platform (UKSeRP). Following approval through safeguard processes, access to project-specific data within the secure environment is permitted using two-factor authentication.",
                    "accessRequestCost": "Data provision is free from SAIL. Overall project costing depends on the number of people that require access to the SAIL Gateway, the activities that SAIL needs to complete (e.g. loading non-standard datasets), data refreshes, analytical work required, disclosure control process, and special case technological requirements.",
                    "deliveryLeadTime": null,
                    "jurisdiction": "GB",
                    "dataProcessor": "SAIL Databank",
                    "dataController": "Welsh Government"
                },
                "formatAndStandards": {
                    "vocabularyEncodingScheme": "LOCAL",
                    "conformsTo": "LOCAL",
                    "language": "en",
                    "format": "SQL database table"
                }
        },
        "enrichmentAndLinkage": {
                "qualifiedRelation": "Yes. To any SAIL dataset & reference data.",
                "derivation": null,
                "tools": "https://conceptlibrary.saildatabank.com/"
        },
        "observations": [
                {
                    "observedNode": "EVENTS",
                    "measuredValue": 3000000,
                    "observationDate": "2021-09-01",
                    "measuredProperty": "Count",
                    "disambiguatingDescription": "Approx 70-80% coverage of Welsh population through GP registrations."
                }
        ],
        "structuralMetadata": [
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "AVAIL_FROM_DT",
                                "description": "Date when the data made available i.e. date of loading",
                                "dataType": "DATE",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "DATEATTENDANCE",
                                "description": "Date of session attendance",
                                "dataType": "DATE",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "ESTAB_E",
                                "description": "Establishment Code - Encrypted",
                                "dataType": "BIGINT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "LEA",
                                "description": "Local Education Area",
                                "dataType": "INTEGER",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "SCHOOLREF_E",
                                "description": "School Reference ID",
                                "dataType": "BIGINT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "SESSION",
                                "description": "-",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "SESSIONTYPE",
                                "description": "To idenitify whether the session was in the morning or afternoon e.g. AM",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "EDAD",
                    "description": "Education Daily Activity Dataset table",
                    "elements": [
                            {
                                "name": "SYSTEM_ID_E",
                                "description": "Local pupil identifier. This is specific to the school and one ALF may have mulitple SYSTEM_ID",
                                "dataType": "BIGINT",
                                "sensitive": false
                            }
                    ]
                }
        ]
    }
    ```

??? example "ALLEVIATE: The 1958 National Child Development Study (NCDS)"

    ```json
    {
        "identifier": "https://web.www.healthdatagateway.org/77dc7118-443c-4c85-a18c-e7bbe01e9e7a",
        "version": "1.0.0",
        "issued": "2021-09-23T00:00:00.000Z",
        "modified": "2021-09-23T00:00:00.000Z",
        "revisions": [],
        "summary": {
                "title": "1958 National Child Development Study - Pain data",
                "abstract": "This collection specifically relates to a short pain survey (self-completion booklet) completed by NCDS participants in 2002-3.",
                "publisher": {
                    "identifier": "https://web.www.healthdatagateway.org/613b2174b8b58d157f531e7a",
                    "name": "ALLEVIATE",
                    "logo": null,
                    "description": null,
                    "contactPoint": null,
                    "memberOf": "HUB"
                },
                "contactPoint": "blah@blah.com",
                "keywords": "Alleviate,Pain,Pain Hub",
                "alternateIdentifiers": null,
                "doiName": "10.5255/UKDA-SN-8731-1"
        },
        "documentation": {
                "description": "The 1958 National Child Development Study (NCDS) is following the lives of an initial 17,415 people born in England, Scotland and Wales in a single week of 1958. It started in 1958 at birth, as the Perinatal Mortality Survey. Over the course of cohort members\u2019 lives, information has been collected on their physical and educational development, economic circumstances, employment, family life, health behaviour, wellbeing, social participation and attitudes.\n\nThis collection specifically relates to a short pain survey (self-completion booklet) completed by NCDS participants in 2002-3.",
                "associatedMedia": "https://discovery.closer.ac.uk/item/uk.cls.ncds/107fe7d5-b871-463e-853c-a592552b591a/1",
                "isPartOf": "https://cls.ucl.ac.uk/cls-studies/1958-national-child-development-study-2/"
        },
        "coverage": {
                "spatial": "https://www.geonames.org/2648147/great-britain.html",
                "typicalAgeRange": "31-59",
                "physicalSampleAvailability": null,
                "followup": "> 10 YEARS",
                "pathway": "Data are not associated with a patient pathway."
        },
        "provenance": {
                "origin": {
                    "purpose": "STUDY",
                    "source": "PAPER BASED",
                    "collectionSituation": "COMMUNITY,HOME"
                },
                "temporal": {
                    "accrualPeriodicity": "STATIC",
                    "distributionReleaseDate": "2004-03-31",
                    "startDate": "2002-09-01",
                    "endDate": "2004-03-31",
                    "timeLag": "1-2 MONTHS"
                }
        },
        "accessibility": {
                "usage": {
                    "dataUseLimitation": "GENERAL RESEARCH USE",
                    "dataUseRequirements": "PROJECT SPECIFIC RESTRICTIONS",
                    "resourceCreator": "UK Data Services",
                    "investigations": "https://www.ukri.org/news/new-data-hub-and-research-into-chronic-pain/",
                    "isReferencedBy": "http://repec.ioe.ac.uk/REPEc/pdf/qsswp2128.pdf"
                },
                "access": {
                    "accessRights": "https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8731#!/access-data",
                    "accessService": "The Data Collection is available to users registered with the UK Data Service.\n\nCommercial use of the data requires approval from the data owner or their nominee. The UK Data Service will contact you.",
                    "accessRequestCost": "https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8731#!/access-data",
                    "deliveryLeadTime": null,
                    "jurisdiction": "GB-GB",
                    "dataProcessor": "George Ploubidis. Professor of Population Health and Statistics at the UCL Social Research Institute.",
                    "dataController": "University College London is the Data Controller and is committed to protecting the rights of individuals in line with the Data Protection Act 2018 (DPA) and the new General Data Protection Regulation (GDPR).\n\nYour test result and unique ID will be retained by Thriva for three years. No other information will be retained by Thriva. The Department for Health and Social Care are the Data Controller for the data that will be retained by Thriva."
                },
                "formatAndStandards": {
                    "vocabularyEncodingScheme": "NHS NATIONAL CODES,OTHER,LOCAL",
                    "conformsTo": "NHS DATA DICTIONARY",
                    "language": "en",
                    "format": "Text"
                }
        },
        "enrichmentAndLinkage": {
                "qualifiedRelation": "https://cls.ucl.ac.uk/data_documentation/?studies%5B%5D=age-42-sweep&studies%5B%5D=substudies&studies%5B%5D=ncds-birth-sweep&studies%5B%5D=age-7-sweep&studies%5B%5D=age-11-sweep&studies%5B%5D=age-16-sweep&studies%5B%5D=age-23-sweep&studies%5B%5D=age-33-sweep&studies%5B%5D=age-44-biomedical-sweep&studies%5B%5D=age-46-sweep&studies%5B%5D=age-50-sweep&studies%5B%5D=age-55-sweep&studies%5B%5D=age-62-sweep&s=&filter=1",
                "derivation": "Not Known",
                "tools": null
        },
        "observations": [
                {
                    "observedNode": "FINDINGS",
                    "measuredValue": 8565,
                    "observationDate": "2002-09-01",
                    "measuredProperty": "Count",
                    "disambiguatingDescription": "Self-reported pain questionnaire"
                }
        ],
        "structuralMetadata": [
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "BE1",
                                "description": "SC1 (E1): Pain during the last month lasting > one day",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "BE2",
                                "description": "SC1 (E2): Have you been aware of this pain for > 3 months",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR1",
                                "description": "SC1 (E3): ACRU Pain Definition - Left Upper",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR2",
                                "description": "SC1 (E3): ACRU Pain Definition - Right Upper",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR3",
                                "description": "SC1 (E3): ACRU Pain Definition - Left Lower",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR4",
                                "description": "SC1 (E3): ACRU Pain Definition - Right Lower",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR5",
                                "description": "SC1 (E3): ACRU Pain Definition - Upper Spine",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR6",
                                "description": "SC1 (E3): ACRU Pain Definition - Left: Low Back",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR7",
                                "description": "SC1 (E3): ACRU Pain Definition - Lower Spine",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR8",
                                "description": "SC1 (E3): ACRU Pain Definition - Right: Low Back",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR9",
                                "description": "SC1 (E3): ACRU Pain Definition - Left Buttock",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_ACR10",
                                "description": "SC1 (E3): ACRU Pain Definition - Right Buttock",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN1",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Shoulder",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN2",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Elbow",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN3",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Forearm",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN4",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Hand",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN5",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Shoulder",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN6",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Elbow",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN7",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Forearm",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN8",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Hand",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN9",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Thigh",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN10",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Knee",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN11",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Lower Leg",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN12",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Foot",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN13",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Thigh",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN14",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Knee",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN15",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Lower Leg",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN16",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Foot",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN17",
                                "description": "SC1 (E3): Manchester Pain Definition - Head",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN18",
                                "description": "SC1 (E3): Manchester Pain Definition - Throat / Sternum",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN19",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Chest",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN20",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Chest",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN21",
                                "description": "SC1 (E3): Manchester Pain Definition - Abdomen",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN22",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Upper Back",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN23",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Upper Back",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN24",
                                "description": "SC1 (E3): Manchester Pain Definition - Upper Spine",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN25",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Low Back",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN26",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Low Back",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN27",
                                "description": "SC1 (E3): Manchester Pain Definition - Lower Spine",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN28",
                                "description": "SC1 (E3): Manchester Pain Definition - Left Buttock",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "NCDS Biomedical Paper Self-Completion 1 (2002) Dataset (85 of 172)",
                    "elements": [
                            {
                                "name": "E3_MAN29",
                                "description": "SC1 (E3): Manchester Pain Definition - Right Buttock",
                                "dataType": "Frequency",
                                "sensitive": false
                            }
                    ],
                    "description": null
                }
        ]
    }
    ```

??? example "NHS Digitial: COVID-19 Vaccination Status"

    ```json
    {
        "identifier": "https://web.www.healthdatagateway.org/c230a8d8-bf78-4713-8f2f-312162e92e55",
        "version": "3.0.0",
        "issued": "2021-10-13T00:00:00.000Z",
        "modified": "2021-10-13T00:00:00.000Z",
        "revisions": [],
        "summary": {
                "title": "COVID-19 Vaccination Status",
                "abstract": "Data relating to coronavirus (COVID-19) vaccination status.",
                "publisher": {
                    "identifier": "https://web.www.healthdatagateway.org/5f86cd34980f41c6f02261f4",
                    "name": "NHS DIGITAL",
                    "logo": null,
                    "description": null,
                    "contactPoint": null,
                    "memberOf": "ALLIANCE"
                },
                "contactPoint": "blah@blah.nhs.uk",
                "keywords": "DIGITRIALS,VACCINATION,ENGLAND,National Core Study,COVID-19,NCS",
                "alternateIdentifiers": null,
                "doiName": null
        },
        "documentation": {
                "description": "Includes: Patient demographics, Source Organisation, vaccination details and vaccine batch events. Its scope covers: \nAnyone vaccinated within England \nAnyone vaccinated in a Devoted Administration where this information is subsequently passed to England.    \n\nSettings include: \nhospital hubs - NHS providers vaccinating on site \nlocal vaccine services \u2013 community or primary care led services which could include primary care facilities, retail, community facilities, temporary structures or roving teams \nvaccination centres \u2013 large sites such as sports and conference venues set up for high volumes of people \n\nTimescales for dissemination can be found under 'Our Service Levels' at the following link: https://digital.nhs.uk/services/data-access-request-service-dars/data-access-request-service-dars-process",
                "associatedMedia": null,
                "isPartOf": null
        },
        "coverage": {
                "spatial": "United Kingdom,England",
                "typicalAgeRange": "16-150",
                "physicalSampleAvailability": null,
                "followup": "OTHER",
                "pathway": null
        },
        "provenance": {
                "origin": {
                    "purpose": "CARE,OTHER",
                    "source": "EPR",
                    "collectionSituation": "PRIMARY CARE,OTHER"
                },
                "temporal": {
                    "accrualPeriodicity": "WEEKLY",
                    "distributionReleaseDate": null,
                    "startDate": "2020-12-08",
                    "endDate": "2021-09-30",
                    "timeLag": "LESS 1 WEEK"
                }
        },
        "accessibility": {
                "usage": {
                    "dataUseLimitation": "RESEARCH SPECIFIC RESTRICTIONS",
                    "dataUseRequirements": "INSTITUTION SPECIFIC RESTRICTIONS,PROJECT SPECIFIC RESTRICTIONS,TIME LIMIT ON USE",
                    "resourceCreator": "NHS DIGITAL",
                    "investigations": "https://digital.nhs.uk/services/data-access-request-service-dars/register-of-approved-data-releases",
                    "isReferencedBy": null
                },
                "access": {
                    "accessRights": "https://digital.nhs.uk/services/data-access-request-service-dars",
                    "accessService": "Once your DARS application has been approved, data will be made available either by secure file transfer or through the Data Access Environment (DAE).\n\nSecure file transfer: https://digital.nhs.uk/services/transfer-data-securely\n\nDAE: https://digital.nhs.uk/services/data-access-environment-dae",
                    "accessRequestCost": "https://digital.nhs.uk/services/data-access-request-service-dars",
                    "deliveryLeadTime": null,
                    "jurisdiction": "GB-ENG",
                    "dataProcessor": null,
                    "dataController": "NHS DIGITAL"
                },
                "formatAndStandards": {
                    "vocabularyEncodingScheme": "SNOMED CT",
                    "conformsTo": "LOCAL",
                    "language": "en",
                    "format": "csv"
                }
        },
        "enrichmentAndLinkage": {
                "qualifiedRelation": "https://digital.nhs.uk/services/data-access-request-service-dars/register-of-approved-data-releases",
                "derivation": "Data will be minimised as appropriate relative to the data access application",
                "tools": "https://digital.nhs.uk/developer/api-catalogue/vaccination-adverse-reactions-covid-19-standards"
        },
        "observations": [
                {
                    "observedNode": "PERSONS",
                    "measuredValue": 17521000,
                    "observationDate": "2021-03-03",
                    "measuredProperty": "Count",
                    "disambiguatingDescription": "People receiving their first dose of a COVID-19 vaccination "
                }
        ],
        "structuralMetadata": [
                {
                    "name": "COVID-19 Vaccination Status",
                    "description": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Person Forename",
                                "description": "Forename of the subject",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Person Surname",
                                "description": "Surname of the subject",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Person Date of Birth",
                                "description": "The Date of Birth of the patient",
                                "dataType": "Date",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Person Gender Code",
                                "description": "Subject administrative gender. Uses national codes from https://datadictionary.nhs.uk/attributes/person_gender_code.html",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Person Postcode",
                                "description": "Subject Postcode. In certain scenarios, the following are to be used: ZZ99 3VZ No Fixed Abode\nZZ99 3VZ Address Not Known; Z99 3CZ Address not specified; V81999 (registered GP Practice Code not known); V81998 (registered GP Practice code not applicable); V81997 (No registered GP Practice)",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Date and Time",
                                "description": "The date and time on which the vaccination intervention was carried out or was meant to be administered",
                                "dataType": "DateTime",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Site Code",
                                "description": "The Site Code (e.g. ODS/ORD) of the organisation that performed the vaccination",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Unique ID",
                                "description": "A unique identifier for the vaccination record, that is consistent between any subsequent update or delete records",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Unique ID URI",
                                "description": "A URI for the system that has allocated the vaccination identifier",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Performing Professional body Registration URI",
                                "description": "A URI for the system that provides the professional body registration codes",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Recorded Date",
                                "description": "The date that the vaccination administered (procedure) or not administered (situation) was recorded in the source system",
                                "dataType": "Date",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Primary Source",
                                "description": "An indication that the content of the record is based on information from the person who administered the vaccine. This reflects the context under which the data was originally recorded. E.g. where data has been captured directly in the source system PRIMARY_SOURCE=True, where it has not (e.g. it has been reported) then PRIMARY_SOURCE=False",
                                "dataType": "Boolean",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Vaccination Procedure Code",
                                "description": "A unique SNOMED Concept Id code relating to vaccine that was administered (procedure) - first or second dose",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Vaccination Situation Code",
                                "description": "Where NOT_GIVEN=True. A unique SNOMED Concept Id code detailing the reason why a vaccination was not administered (situation)",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Vaccination Not Given",
                                "description": "A flag to indicate if the vaccination was NOT given",
                                "dataType": "Boolean",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Reason Not Given Code",
                                "description": "Where NOT_GIVEN=True. A unique SNOMED Concept Id code giving the reason why a vaccination was not administered",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Dose Sequence",
                                "description": "Nominal position in a series of vaccines.",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Vaccine Product Code",
                                "description": "Unique SNOMED Concept Id code specifying what vaccine product was administered",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Expiry Date",
                                "description": "Earlier of either: Manufacturer expiry date of the vaccine OR Coronavirus point of care sites will only put in the defrost expiry date",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Site of Vaccination Code",
                                "description": "Unique SNOMED Concept Id code specifying the body site vaccine was administered into",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Route of Vaccination Code",
                                "description": "Unique SNOMED Concept Id code detailing how vaccine entered the body (N.B. Coronavirus vaccination are only administered via the intramuscular route)",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Dose Amount",
                                "description": "Amount of vaccine administered. For example: 1, 1.0 or 1.5",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Dose Unit Code",
                                "description": "A dm+d (SNOMED) Concept ID value representing the Unit of measure used",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Indication Code",
                                "description": "A SNOMED Concept Id value representing the clinical indication or reason for administering or recording an historical vaccination",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "NHS Number Status Indicator Code",
                                "description": "The trace status code of the NHS NUMBER (where provided). Code value from https://datadictionary.nhs.uk/attributes/nhs_number_status_indicator_code.html?hl=trace",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Site Code Type URI",
                                "description": "A code value indicating the type of site code value provided",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Consent for Treatment Code",
                                "description": "SNOMED Concept ID (where available) relating to consent for treatment",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Care Setting Type Code",
                                "description": "SNOMED Concept ID for Care Setting where the vaccination information has been captured e.g. the code for Community Health Services for NHS Staff",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Sending Organisation Code",
                                "description": "A code to denote the organisation sending the data. Note; This is a code identifying the sending system/organisation rather than the organisation who administered the vaccination",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Token Person ID",
                                "description": "This field contains a pseudonymised unique identifier for each individual patient.",
                                "dataType": "Nvarchar",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Month and Year of Birth",
                                "description": "Month and year, derived from birth date MMYYYY",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Age",
                                "description": "Age in years at point of vaccination, derived from date of birth",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Postcode District",
                                "description": "Postcode district, derived from postcode",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Lower Layer Super Output Area (LSOA)",
                                "description": "2011 Census Lower Layer Super Output Area (LSOA)/ Super Output Area (SOA)/ Data Zone (DZ). Derived from subjects postcode using ONS UK Postcode file (LSOA11)",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Trace Verified",
                                "description": "Has the patient been traced? Derived from exceptions reason",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Vaccination Unique ID",
                                "description": "Foreign key, which refers to the unique identifier for the vaccination record, with which these screening question responses are associated.",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Vaccination Unique ID URI",
                                "description": "Foreign key, which refers to the URI for the system that has been allocated the vaccination identifier.",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Attribute ID",
                                "description": "3-digit unique identifier for the attribute being evaluated.",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Attribute Displayed Text",
                                "description": "A de-normalised copy of the attribute text used in the vaccination event.",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Attribute Value",
                                "description": "A value indicating the response given by the patient to the ATTRIBUTE_ID question.",
                                "dataType": "String",
                                "sensitive": false
                            }
                    ],
                    "description": null
                },
                {
                    "name": "COVID-19 Vaccination Status",
                    "elements": [
                            {
                                "name": "Recorded Date2",
                                "description": "The date which the extended attribute event occurred",
                                "dataType": "Date",
                                "sensitive": false
                            }
                    ],
                    "description": null
                }
        ]
    }

??? example "PIONEER: Deeply phenotyped sepsis patients within hospital: onset, treatments & outcomes"

    ```json
    {
        "identifier": "https://web.www.healthdatagateway.org/273e091c-d0b3-4529-9cd2-4bc1a1b6195a",
        "version": "2.0.0",
        "issued": "2021-02-26T00:00:00.000Z",
        "modified": "2021-02-26T00:00:00.000Z",
        "revisions": [],
        "summary": {
                "title": "Deeply phenotyped sepsis patients within hospital: onset, treatments & outcomes",
                "abstract": "Hospitalised sepsis patients (2000-2020) by cause. Deeply phenotyped, longitudinal.  Granular ethnicity and multi-morbidity.  Serial acuity, physiology, blood parameters, treatments, interventions, ITU spells, outcomes, pre and post sepsis healthcare.",
                "publisher": {
                    "identifier": "https://web.www.healthdatagateway.org/607db9c5e1f9d3704d570d5f",
                    "name": "PIONEER",
                    "logo": null,
                    "description": null,
                    "contactPoint": "blah@blah.NHS.UK",
                    "memberOf": "HUB"
                },
                "contactPoint": "blah@blah.NHS.UK",
                "keywords": "Sepsis,Infection,NHS,Acute,immune system,life-threatening,septicaemia,blood-poisoning,MOF,organ failure,respiratory tract,pneumonia,urinary tract,hepatobiliary,central nervous system,cellulitis,osteomyelitus,endocarditis,viral,bacterial,fungal,blood biomarkers,microbiology,treatments,antibiotics,physiology,serial readings,outcomes,intensive care,death,discharge,length of stay,multi-morbidity,COVID-19,wave 1,wave 2",
                "alternateIdentifiers": null,
                "doiName": null
        },
        "documentation": {
                "description": "Deeply phenotyped sepsis patients within hospital: onset, treatments & outcomes \n\nSepsis is life-threatening organ dysfunction due to a dysregulated host response to infection & is a global health challenge. In 2017, 48\u20229 million incident cases of sepsis were recorded worldwide with 11million sepsis-related deaths, representing 19\u20227% of all global deaths. There are >123,000 sepsis cases diagnosed in Engl& each year with an estimated 36,800 sepsis-associated deaths.   Sepsis is treatable, & timely, targeted interventions improve outcomes.  The World Health Assembly identified sepsis as a global health priority. \n\nPIONEER geography\nThe West Midlands (WM) has a population of 5.9 million & includes a diverse ethnic & socio-economic mix. There is a higher than average percentage of minority ethnic groups. WM has a large number of elderly residents but is the youngest population in the UK.  Birmingham has the highest birth rate in England.  It also has the highest infant mortality rate. WM life expectancy is 1.8 years less than in London. There are particularly high rates of physical inactivity, obesity, smoking & diabetes.  Each day >100,000 people are treated in hospital, see their GP or are cared for by the NHS.\n\nEHR. University Hospitals Birmingham NHS Foundation Trust (UHB) is one of the largest NHS Trusts in England, providing direct acute services & specialist care across four hospital sites, with 2.2 million patient episodes per year, 2750 beds & 100 ITU beds. UHB runs a fully electronic healthcare record (EHR) (PICS; Birmingham Systems), a shared primary & secondary care record (Your Care Connected) & a patient portal \u201cMy Health\u201d. \n\nScope: All hospitalised patients to UHB from 2000 \u2013 current day.  Updated monthly.  Longitudinal & individually linked, so that the preceding & subsequent health journey can be mapped & healthcare utilisation prior to & after sepsis understood.\nThe dataset includes ICD-10 & SNOMED-CT codes pertaining to sepsis & suspected sepsis.  Serial, structured data pertaining to process of care (timings, staff grades, specialty review, wards), presenting complaint, all physiology readings (pulse, blood pressure, respiratory rate, oxygen saturations), all blood results, microbiology, all prescribed & administered treatments (fluids, antibiotics, inotropes, vasopressors, organ support), all outcomes.  Linked images available (radiographs, CT, MRI, ultrasound). Includes COVID-19 wave 1 and wave 2 data.\n\nAvailable supplementary data:\nMatched \u201cnon-sepsis\u201d controls; ambulance, 111, 999 data, synthetic data.\n\nAvailable supplementary support: Analytics, Model build, validation & refinement; A.I.; Data partner support for ETL (extract, transform & load) process, Clinical expertise, Patient & end-user access, Purchaser access, Regulatory requirements, Data-driven trials, \u201cfast screen\u201d services.",
                "associatedMedia": "https://www.pioneerdatahub.co.uk/wp-content/uploads/Sepsis-Infographic-V3.pdf",
                "isPartOf": null
        },
        "coverage": {
                "spatial": "United Kingdom,England,West Midlands",
                "typicalAgeRange": "0-110",
                "physicalSampleAvailability": null,
                "followup": "OTHER",
                "pathway": "Data focuses on in-patient stay in hospital during the sepsis episode but can be supplemented on request to include previous and subsequent hospital contacts (including outpatient appointments) and ambulance, 111, 999 data."
        },
        "provenance": {
                "origin": {
                    "purpose": "OTHER",
                    "source": "EPR",
                    "collectionSituation": "IN-PATIENTS"
                },
                "temporal": {
                    "accrualPeriodicity": "QUARTERLY",
                    "distributionReleaseDate": "2020-11-19",
                    "startDate": "2018-01-01",
                    "endDate": "2020-11-19",
                    "timeLag": "LESS 1 WEEK"
                }
        },
        "accessibility": {
                "usage": {
                    "dataUseLimitation": "GENERAL RESEARCH USE",
                    "dataUseRequirements": "PROJECT SPECIFIC RESTRICTIONS",
                    "resourceCreator": "\"This work was supported by PIONEER, the Health Data Research Hub in acute care\".  If publishing using PIONEER overarching ethics, state                                                    \"This research was conducted under the ethical approvals of PIONEER, a Health data research hub in acute care (East Midlands \u2013 Derby Research ethics committee, reference 20/EM/0158)\".",
                    "investigations": null,
                    "isReferencedBy": "Sapey E, Gallier S, Mainey C All clinicians and students at University Hospitals Birmingham NHS Foundation Trust, et al Ethnicity and risk of death in patients hospitalised for COVID-19 infection in the UK: an observational cohort study in an urban catchment area BMJ Open Respiratory Research 2020;7:e000644. doi: 10.1136/bmjresp-2020-000644      ,Phagura, Nuvreen & Thandi, Karanjeet & Evison, Felicity & Gallier, Suzy & Sharif, Adnan. (2020). P1724RISK FACTORS FOR BK VIRUS INFECTION AFTER KIDNEY TRANSPLANTATION IN THE CONTEMPORARY ERA: A SINGLE-CENTRE OBSERVATIONAL STUDY. Nephrology Dialysis Transplantation. 35. 10.1093/ndt/gfaa142.P1724.  ,Shallcross, L.J., Freemantle, N., Nisar, S. et al. A cross-sectional study of blood cultures and antibiotic use in patients admitted from the Emergency Department: missed opportunities for antimicrobial stewardship. BMC Infect Dis 16, 166 (2016). https://doi.org/10.1186/s12879-016-1515-1 ,Shallcross, L.J., Rockenschaub, P., McNulty, D. et al. Diagnostic uncertainty and urinary tract infection in the emergency department: a cohort study from a UK hospital. BMC Emerg Med 20, 40 (2020). https://doi.org/10.1186/s12873-020-00333-y"
                },
                "access": {
                    "accessRights": "https://www.pioneerdatahub.co.uk/data/data-request-process/",
                    "accessService": "Trusted Research Environments (TRE) are built using Microsoft Azure services and hosted in the UK to provide research teams a safe, secure and agile environment which allows users to quickly analyse, interpret and form an enriched view of primary care information through a range of integrated datasets.\n\nHealth data collated from multiple sources is ingested into a secure data lake which will then allow subsets of data to be made available to research teams on approval of a data request. Once approved a customer specific TRE is made available with a standard set of leading analytical tools from Microsoft including Azure Databricks, Azure Machine Learning, Azure SQL and Azure Synapse (for large-scale data warehouses). Specific tools can be provided at an additional cost over the standard platform data access charge and the PIONEER team will work with you to determine your exact needs.\n\nAccess to the TRE is managed using the latest virtual desktop technology to provide a safe and secure end-user experience.  By utilising leading edge design PIONEER are able to create TREs rapidly to enable us to service any customer requirement.",
                    "accessRequestCost": "www.pioneerdatahub.co.uk/data/data-services-costs/",
                    "deliveryLeadTime": null,
                    "jurisdiction": "GB",
                    "dataProcessor": null,
                    "dataController": "University Hospitals Birmingham NHS Foundation Trust"
                },
                "formatAndStandards": {
                    "vocabularyEncodingScheme": "SNOMED CT,ICD10",
                    "conformsTo": "LOCAL",
                    "language": "en",
                    "format": "SQL"
                }
        },
        "enrichmentAndLinkage": {
                "qualifiedRelation": null,
                "derivation": null,
                "tools": null
        },
        "observations": [
                {
                    "observedNode": "EVENTS",
                    "measuredValue": -1,
                    "observationDate": "2020-11-19",
                    "measuredProperty": "count",
                    "disambiguatingDescription": "Not applicable"
                }
        ],
        "structuralMetadata": [
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "spell_id",
                                "description": "Spell identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diagnosis_end",
                                "description": "End date of diagnosis",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diagnosis_start_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diag_snomed",
                                "description": "Diagnosis snomed code",
                                "dataType": "BIGINT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diag_snomed_expn",
                                "description": "Diagnosis snomed concept",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diag_icd10",
                                "description": "ICD10 code",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diagnosis_time_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diagnosis_end_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diagnosis_start",
                                "description": "Start date of diagnosis",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "precedence",
                                "description": "Order of diagnosis",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diagnosis_id",
                                "description": "Unique diagnosis identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDiagnosis",
                    "description": "Diagnosis details for each spell",
                    "elements": [
                            {
                                "name": "diagnosis_time",
                                "description": "Time of diagnosis",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "spell_end",
                                "description": "Patient spell end date",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "first_sews",
                                "description": "First SEWS score",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "itu_hdu_start",
                                "description": "Intensive care unit start date",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "spell_start_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "admission_source",
                                "description": "Source of admission",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "admission_type",
                                "description": "Type of admission",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "imd_decile",
                                "description": "Index of multiple deprivation decile score based off postcode (1 is most deprived 10 is least deprived)",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "itu_hdu_start_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "itu_hdu_end",
                                "description": "Intensive care unit end date",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "date_of_birth",
                                "description": "date of birth",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "first_news2",
                                "description": "First NEWS2 score",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "itu_hdu_end_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "covid_symptom_duration",
                                "description": "Duration of suspected corona virus 2019 in days",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "discharge_outcome",
                                "description": "Discharge outcome",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "patient_id",
                                "description": "Hashed patient identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "sex",
                                "description": "Patient sex",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "imd_quintile",
                                "description": "Index of multiple deprivation quintile score based off postcode (1 is most deprived 5 is least deprived)",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "spell_id",
                                "description": "Unique spell identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "spell_end_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "ethnicity",
                                "description": "Patient ethnicity",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "spell_start",
                                "description": "Patient spell start date",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "date_of_death",
                                "description": "Date of death",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisAdmission",
                    "description": "Spell admission details",
                    "elements": [
                            {
                                "name": "postcode",
                                "description": "Patient postcode",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "quantity_units",
                                "description": "Quantity units",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "frequency",
                                "description": "frequency of drug administered",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "volume_remaining",
                                "description": "Volume remaining",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "concentration_units",
                                "description": "Concentration units",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "time_administered_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "concentration",
                                "description": "Concentration",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "time_prescribed",
                                "description": "Prescibed time",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "spell_id",
                                "description": "Spell identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "time_written_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "infusion_rate",
                                "description": "Rate of infusion",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "time_prescribed_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "form",
                                "description": "Drug form",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "drug_administration_id",
                                "description": "Unique drug administration identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "time_written",
                                "description": "Prescription written time",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "drug",
                                "description": "Type of drug",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "time_administered",
                                "description": "Administered time",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "mode",
                                "description": "mode of drug administered",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "infusion_rate_units",
                                "description": "Infusion units",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "route",
                                "description": "Administered route",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisDrugAdmin",
                    "description": "Drug administered for each spell",
                    "elements": [
                            {
                                "name": "quantity",
                                "description": "Quantity",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "spell_id",
                                "description": "Spell identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "time_preformed",
                                "description": "Measurement preformed time",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "result",
                                "description": "Numerical result of the measurement",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "time_requested_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "measurement_id",
                                "description": "Unique measurement identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "result_expn",
                                "description": "SNOMED concept describing the result (if applicable)",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "specimen_id",
                                "description": "specimen identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "measurement_scid",
                                "description": "Measurement snomed concept",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "units",
                                "description": "SNOMED concept describing the units of the result",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "time_preformed_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "measurement",
                                "description": "Measurement name",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "result_qualifier",
                                "description": "SNOMED concept describing any operator applied to a numerical result e.g. \"<=\" or 'estimated'",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisMeasurement",
                    "description": "Measurement detail for each spell",
                    "elements": [
                            {
                                "name": "time_requested",
                                "description": "Measurement request time",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "imaging_id",
                                "description": "Unique image identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "time_completed_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "exam_name",
                                "description": "Image examination name",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "image_type",
                                "description": "Type of image",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "spell_id",
                                "description": "Spell identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "time_completed",
                                "description": "Imaging completion date",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "time_requested",
                                "description": "Request time for imaging",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "location",
                                "description": "Referring location",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisImaging",
                    "description": "Imaging detail for each spell",
                    "elements": [
                            {
                                "name": "time_requested_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "site_move_id",
                                "description": "Unique site move identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "move_time",
                                "description": "Ward move date",
                                "dataType": "DATETIME",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "spell_id",
                                "description": "Spell identification",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "move_time_day_type",
                                "description": "Describes the type of day, whether it was a 'working day', 'public holiday' or 'weekend '",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "move_order_desc",
                                "description": "Ward move order in descending order",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "site_code",
                                "description": "Site and ward code",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "move_order_asc",
                                "description": "Ward move order in ascending order",
                                "dataType": "INT",
                                "sensitive": false
                            }
                    ]
                },
                {
                    "name": "SepsisWardMove",
                    "description": "WardMove detail for each spell",
                    "elements": [
                            {
                                "name": "site",
                                "description": "Site and ward name",
                                "dataType": "VARCHAR",
                                "sensitive": false
                            }
                    ]
                }
        ]
    }

### HDRUK 2.2.0 Schema

These payloads (`{"metadata":<json>}`) will validate (return status `200`) against TRASER (translation service) endpoint:

`/validate?input_schema=HDRUK&input_version=2.2.0`

This new schema allows a few additional fields and includes a section for adding tissue data.

The change log for this schema can be found at:
[https://hdruk.github.io/schemata-2/HDRUK/2.2.0.change/](https://hdruk.github.io/schemata-2/HDRUK/2.2.0.change/)

??? example "PHS: COVID19 in Pregnancy in Scotland (COPS)"

    ```json
    {
        "identifier": "https://web.www.healthdatagateway.org/cc198cd8-0fca-4d4b-95a5-f0d5df0719e2",
        "version": "1.0.0",
        "issued": "2023-07-19T00:00:00.000Z",
        "modified": "2023-07-19T00:00:00.000Z",
        "revisions": [],
        "summary": {
            "title": "COVID19 in Pregnancy in Scotland (COPS)",
            "abstract": "The COPS study is a sub study to Early Pandemic Evaluation and Enhanced Surveillance of COVID-19 (EAVE II)\n\nThe cohort includes all pregnant women who could have potentially been exposed to SARS-2-CoV (from March 2020) or COVID-19 vaccination. ",
            "publisher": {
                "identifier": "https://web.www.healthdatagateway.org/5f8992a97150a1b050be0712",
                "name": "PUBLIC HEALTH SCOTLAND",
                "logo": null,
                "description": null,
                "contactPoint": null,
                "memberOf": "ALLIANCE"
            },
            "contactPoint": "blah@blah.scot",
            "keywords": "COVID-19,Pregnancy,Public Health Scotland",
            "alternateIdentifiers": null,
            "doiName": null,
            "datasetType": "Population Level",
            "datasetSubType": "Population Level",
            "populationSize": 0
        },
        "documentation": {
            "description": "COPS linked healthcare records on all pregnancies in Scotland including early pregnancy losses (eg miscarriage, ectopic pregnancy), terminations of pregnancy, live and stillbirths and neonatal health records, with COVID-19 test results and COVID-19 vaccine records. The COPS dataset links together variables from a wide range of source datasets including GP records.\n\n",
            "associatedMedia": null,
            "isPartOf": null
        },
        "coverage": {
            "spatial": "United Kingdom,Scotland",
            "typicalAgeRange": null,
            "followup": null,
            "pathway": null,
            "biologicalsamples": null,
            "gender": null,
            "psychological": null,
            "physical": null,
            "anthropometric": null,
            "lifestyle": null,
            "socioeconomic": null
        },
        "provenance": {
            "origin": {
                "purpose": "STUDY",
                "source": "EPR",
                "collectionSituation": "IN-PATIENTS,PRIMARY CARE"
            },
            "temporal": {
                "distributionReleaseDate": "2022-08-30",
                "startDate": "2015-01-01",
                "endDate": "2022-08-30",
                "timeLag": null,
                "publishingFrequency": "STATIC"
            }
        },
        "accessibility": {
            "usage": {
                "dataUseLimitation": "RESEARCH SPECIFIC RESTRICTIONS",
                "dataUseRequirements": null,
                "resourceCreator": null,
                "investigations": null,
                "isReferencedBy": null
            },
            "access": {
                "accessRights": "https://www.isdscotland.org/Products-and-Services/eDRIS/",
                "accessService": "Scottish National Safe Haven - https://www.isdscotland.org/Products-and-Services/eDRIS/",
                "accessRequestCost": "Research Projects - https://www.isdscotland.org/Products-and-Services/eDRIS/ , Bespoke data analysis requests - https://publichealthscotland.scot/contact-us/bespoke-data-analysis-requests/",
                "deliveryLeadTime": null,
                "jurisdiction": "GB-GBN,GB-SCT",
                "dataProcessor": null,
                "dataController": "Public Health Scotland"
            },
            "formatAndStandards": {
                "vocabularyEncodingScheme": "NHS SCOTLAND NATIONAL CODES,READ",
                "conformsTo": "NHS SCOTLAND DATA DICTIONARY",
                "language": "en",
                "format": "text, csv"
            }
        },
        "enrichmentAndLinkage": {
            "qualifiedRelation": null,
            "derivation": null,
            "tools": null
        },
        "observations": [
            {
                "observedNode": "EVENTS",
                "measuredValue": 526608,
                "observationDate": "2015-01-01",
                "measuredProperty": "Count",
                "disambiguatingDescription": null
            }
        ],
        "structuralMetadata": [],
        "tissuesSampleCollection": null
    }

    ```

??? example "UK Biobank"

    ```json
    {
        "identifier": "https://web.www.healthdatagateway.org/1460e2b4-a985-4890-8e60-a21e78ce01f3",
        "version": "2.0.0",
        "issued": "2022-04-19T00:00:00.000Z",
        "modified": "2022-04-19T00:00:00.000Z",
        "revisions": [],
        "summary": {
            "title": "UK Biobank",
            "abstract": "UK Biobank is a large-scale biomedical database and research resource that provides researchers access to detailed longitudinal phenotype, medical and genetic data from 500,000 volunteer participants. ",
            "publisher": {
                "identifier": "https://web.www.healthdatagateway.org/607db9c6e1f9d3704d570d7f",
                "name": "UK Biobank",
                "logo": null,
                "description": null,
                "contactPoint": null,
                "memberOf": "ALLIANCE"
            },
            "contactPoint": "access@ukbiobank.ac.uk",
            "keywords": "UK BIOBANK,Genomics,Exome sequencing,WGS,Omics,Pain,Research,Cognitive Measures,Physical Measures,Magnetic resonance imaging,DXA,ECG,Accelerometer,Mental Health,Environment,Primary Care,COVID-19,Hospital episode statistics,Cancer Registry,Deaths,Sociodemographics,Digestive Health,Occupational Health,Biomarkers,Lifestyle,Health Data,Cardiac MRI,Brain MRI,Abdominal MRI,Carotid Ultrasound,Diet,Pain Hub",
            "alternateIdentifiers": null,
            "doiName": null,
            "datasetType": "Biobank",
            "datasetSubType": "Biobank",
            "populationSize": 500000
        },
        "documentation": {
            "description": "UK Biobank is a large-scale biomedical database and research resource, containing in-depth genetic and health information from half a million UK participants. The database, which is regularly augmented with additional data, is globally accessible to approved researchers and scientists undertaking vital research into the most common and life-threatening diseases. UK Biobank’s research resource is a major contributor to the advancement of modern medicine and treatment and has enabled several scientific discoveries that improve human health.\n\nSince 2006, UK Biobank has collected an unprecedented amount of biological and medical data on half a million people, aged between 40 and 69 years old and living in the UK, as part of a large-scale prospective study. With their consent they regularly provide blood, urine and saliva samples, as well as detailed information about their lifestyle which is then linked to their health-related records to provide a deeper understanding of how individuals experience diseases. Genotyping, whole exome sequencing and whole genome sequencing is available for the whole cohort. Blood and urine biomarkers, telomere data, metabolomic and proteomic data and infectious disease markers have been assayed from the samples provided.\n\nSince 2014 we have been undertaking the largest imaging study to date. We aim to undertake brain, cardiac and neck to knee MRI, whole body DXA and carotid ultrasound of 100,000 participants. We additionally have retinal images for 100,000 participants from baseline assessment, and accelerometer data for 100,000 participants collected 2013-2014.\n\nQuestionnaires that aim to capture data that is not readily captured by health data linkages are regularly sent to our participants.\n\nThe data – the largest and richest dataset of its kind – is de-identified and made widely accessible by UK Biobank to registered researchers around the world who use it to make new scientific discoveries about common and life-threatening diseases – such as cancer, heart disease and stroke – in order to improve public health.",
            "associatedMedia": "https://biobank.ndph.ox.ac.uk/showcase/index.cgi,https://www.ukbiobank.ac.uk/",
            "isPartOf": null
        },
        "coverage": {
            "spatial": "United Kingdom",
            "typicalAgeRange": "40-69",
            "followup": "CONTINUOUS",
            "pathway": "UK Biobank is a volunteer based cohort. As such, there is a healthy volunteer effect that results in participants tending to be of higher socioeconomic status, remaining in education longer, slimmer, less smokers (although those that smoke tend to be heavier smokers) and lower consumers of alcohol than the general population. A comparison between UK Biobank participants and the general UK population has been published (https://doi.org/10.1093/aje/kwx246).\n\nWhilst selection biases are seen in UK Biobank, there is still substantial heterogeneity within the cohort. Whilst incidence and prevalence calculations are not generalisable to the UK population, exposure-outcome comparisons should be due to the heterogeneity in the cohort. However, it is important that researchers consider the potential biases of a data set that might limit generalisability of their results (as is the case for all observational data). ",
            "biologicalsamples": [
                "Saliva",
                "Urine"
            ],
            "gender": null,
            "psychological": null,
            "physical": null,
            "anthropometric": null,
            "lifestyle": null,
            "socioeconomic": null
        },
        "provenance": {
            "origin": {
                "purpose": "STUDY",
                "source": "EPR,ELECTRONIC SURVEY,MACHINE GENERATED",
                "collectionSituation": "PRIMARY CARE,ACCIDENT AND EMERGENCY,IN-PATIENTS,COMMUNITY,CLINIC,PHARMACY"
            },
            "temporal": {
                "distributionReleaseDate": null,
                "startDate": "2006-03-13",
                "endDate": null,
                "timeLag": "VARIABLE",
                "publishingFrequency": "CONTINUOUS"
            }
        },
        "accessibility": {
            "usage": {
                "dataUseLimitation": "GENERAL RESEARCH USE",
                "dataUseRequirements": "INSTITUTION SPECIFIC RESTRICTIONS,PROJECT SPECIFIC RESTRICTIONS,PUBLICATION REQUIRED,RETURN TO DATABASE OR RESOURCE,USER SPECIFIC RESTRICTION,TIME LIMIT ON USE",
                "resourceCreator": "UK Biobank",
                "investigations": "https://www.ukbiobank.ac.uk/enable-your-research/approved-research",
                "isReferencedBy": "Sudlow C, Gallacher J, Allen N, Beral V, Burton P, Danesh J, et al. (2015) UK Biobank: An Open Access Resource for Identifying the Causes of a Wide Range of Complex Diseases of Middle and Old Age. PLoS Med 12(3): e1001779. https://doi.org/10.1371/journal.pmed.1001779,Bycroft, C., Freeman, C., Petkova, D. et al. The UK Biobank resource with deep phenotyping and genomic data. Nature 562, 203–209 (2018). https://doi.org/10.1038/s41586-018-0579-z,Conroy M, Sellors J, Effingham M, et al. The advantages of UK Biobank’s open-access strategy for health research. J Intern Med. 2019;286(4):389-397. doi:10.1111/joim.12955,Littlejohns TJ, Holliday J, Gibson LM, et al. The UK Biobank imaging enhancement of 100,000 participants: rationale, data collection, management and future directions. Nat Commun. 2020;11(1):2624. doi:10.1038/s41467-020-15948-9,Fry A, Littlejohns TJ, Sudlow C, et al. Comparison of Sociodemographic and Health-Related Characteristics of UK Biobank Participants With Those of the General Population. Am J Epidemiol. 2017:1-9. doi:10.1093/aje/kwx246"
            },
            "access": {
                "accessRights": "https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access",
                "accessService": "Applications to access data are made through our bespoke access management system (https://bbams.ndph.ox.ac.uk/ams/). \n\nData access is either via data download (phenotype and genotype data) or via our Research Analysis Platform (phenotype, imaging, genotype, WES, WGS, omics). Our RAP is enabled by DNANexus and hosted by Amazon Web Services (https://www.ukbiobank.ac.uk/enable-your-research/research-analysis-platform). \n\nAccess costs depend on what data access is required.",
                "accessRequestCost": "https://www.ukbiobank.ac.uk/enable-your-research/costs",
                "deliveryLeadTime": null,
                "jurisdiction": "GB-ENG",
                "dataProcessor": "UK Biobank",
                "dataController": "UK Biobank"
            },
            "formatAndStandards": {
                "vocabularyEncodingScheme": "LOCAL,OPCS4,READ,SNOMED CT,DM+D,ICD10,ICD9",
                "conformsTo": "DICOM,LOCAL,NHS DATA DICTIONARY",
                "language": "en",
                "format": "Text/csv, dta, SAS, R,Image/ DICOM, NIFTI, PNG,Other/ VCF, CRAM, PLINK, BGEN, BED, CWA"
            }
        },
        "enrichmentAndLinkage": {
            "qualifiedRelation": null,
            "derivation": null,
            "tools": null
        },
        "observations": [
            {
                "observedNode": "PERSONS",
                "measuredValue": 500000,
                "observationDate": "2006-03-13",
                "measuredProperty": "Count",
                "disambiguatingDescription": "Each participant has a large number (<5000) of data points associated with them. Recruitment started in 2006, but data collection is ongoing, and health data predates recruitment date. Summary statistics of all data can be found on our data showcase."
            }
        ],
        "structuralMetadata": [
            {
                "name": "UK Biobank Data Dictionary",
                "elements": [
                    {
                        "name": 3,
                        "description": "Verbal interview duration",
                        "dataType": "Integer",
                        "sensitive": false
                    }
                ],
                "description": null
            }
        ],
        "tissuesSampleCollection": [
            {
                "materialType": [
                    "Serum"
                ],
                "dataCategories": null,
                "tissueSampleMetadata": null,
                "collectionType": null
            },
            {
                "materialType": [
                    "Plasma"
                ],
                "dataCategories": null,
                "tissueSampleMetadata": null,
                "collectionType": null
            },
            {
                "materialType": [
                    "Blood"
                ],
                "dataCategories": null,
                "tissueSampleMetadata": null,
                "collectionType": null
            },
            {
                "materialType": [
                    "Saliva"
                ],
                "dataCategories": null,
                "tissueSampleMetadata": null,
                "collectionType": null
            },
            {
                "materialType": [
                    "Urine"
                ],
                "dataCategories": null,
                "tissueSampleMetadata": null,
                "collectionType": null
            }
        ]
    }
    ```

### HDRUK 3.0.0 Schema

    ```json
    {
        "identifier": "https://web.www.healthdatagateway.org/19525c5f-92ee-41b6-bb79-673624b27bdd",
        "version": "3.0.0",
        "issued": "2021-05-10T00:00:00.000Z",
        "modified": "2021-05-10T00:00:00.000Z",
        "revisions": [],
        "summary": {
            "title": "Improving Access to Psychological Therapies Data Set",
            "abstract": "Patient-level data set that captures information about people in contact with services commissioned as part of the adult Improving Access to Psychological Services (IAPT) programme.",
            "contactPoint": "enquiries@nhsdigital.nhs.uk",
            "keywords": " Depression,Anxiety,CBT,Counselling,Talking theraphy,Cognitive,National Core Study,NCS",
            "alternateIdentifiers": null,
            "doiName": null,
            "populationSize": -1,
            "dataProvider": {
                "identifier": "https://web.www.healthdatagateway.org/5f86cd34980f41c6f02261f4",
                "name": "NHS DIGITAL",
                "logo": null,
                "description": null,
                "contactPoint": null,
                "memberOf": "ALLIANCE"
            }
        },
        "documentation": {
            "description": "Collecting information about people in contact with adult psychological therapy services in England. The IAPT data set was developed with the IAPT programme as a patient level, output based, secondary uses data set which aims to deliver robust, comprehensive, nationally consistent and comparable information for patients accessing NHS-funded IAPT services in England. This national data set has been collected since April 2012 and is a mandatory submission for all NHS funded care, including care delivered by independent sector healthcare providers. Data collection on patients with depression and anxiety disorders that are offered psychological therapies, so that we can improve the delivery of care for these conditions.\n\nProviders of NHS-funded IAPT services are required to submit data to NHS Digital on a monthly basis.\n\nAs a secondary uses data set the IAPT data set re-uses clinical and operational data for purposes other than direct patient care. It defines the data items, definitions and associated value sets extracted or derived from local information systems and sent to NHS Digital for analysis purposes. Timescales for dissemination can be found under 'Our Service Levels' at the following link: https://digital.nhs.uk/services/data-access-request-service-dars/data-access-request-service-dars-process",
            "associatedMedia": null,
            "inPipeline": null
        },
        "coverage": {
            "spatial": "United Kingdom,England",
            "followup": "0 - 6 MONTHS",
            "pathway": null,
            "gender": null,
            "typicalAgeRangeMin": 18,
            "typicalAgeRangeMax": 150,
            "datasetCompleteness": null,
            "materialType": [
                "None/not available"
            ]
        },
        "provenance": {
            "origin": {
                "purpose": [
                    "Other",
                    "Administrative"
                ],
                "source": [
                    "EPR"
                ],
                "datasetType": "Health and disease",
                "datasetSubType": "Not applicable",
                "collectionSource": null,
                "imageContrast": null
            },
            "temporal": {
                "distributionReleaseDate": null,
                "startDate": "2012-04-01",
                "endDate": null,
                "timeLag": "2-6 months",
                "publishingFrequency": "Monthly"
            }
        },
        "accessibility": {
            "usage": {
                "dataUseLimitation": [
                    "No restriction"
                ],
                "dataUseRequirements": null,
                "resourceCreator": null
            },
            "access": {
                "accessRights": "https://digital.nhs.uk/services/data-access-request-service-dars",
                "accessService": "Once your DARS application has been approved, data will be made available either by secure file transfer or through the Data Access Environment (DAE). BL\n\nSecure file transfer: https://digital.nhs.uk/services/transfer-data-securely\n\nDAE: https://digital.nhs.uk/services/data-access-environment-dae",
                "accessRequestCost": "https://digital.nhs.uk/services/data-access-request-service-dars/data-access-request-service-dars-charges",
                "deliveryLeadTime": null,
                "jurisdiction": "GB-ENG",
                "dataProcessor": null,
                "dataController": "NHS DIGITAL",
                "accessServiceCategory": null,
                "accessMode": "New project"
            },
            "formatAndStandards": {
                "vocabularyEncodingScheme": [
                    "ODS",
                    "SNOMED CT",
                    "NHS NATIONAL CODES",
                    "ICD10"
                ],
                "conformsTo": [
                    "NHS DATA DICTIONARY"
                ],
                "language": "en",
                "format": "CSV"
            }
        },
        "enrichmentAndLinkage": {
            "tools": null,
            "derivedFrom": null,
            "isPartOf": null,
            "linkableDatasets": null,
            "similarToDatasets": null,
            "publicationAboutDataset": null,
            "investigations": null,
            "publicationUsingDataset": null
        },
        "observations": [
            {
                "observedNode": "Event",
                "measuredValue": 114125,
                "measuredProperty": "COUNT",
                "observationDate": "2021-02-25",
                "disambiguatingDescription": "In December 2020 there were 114,125 referrals made into IAPT services in England."
            },
            {
                "observedNode": "Event",
                "measuredValue": 81578,
                "measuredProperty": "COUNT",
                "observationDate": "2021-02-25",
                "disambiguatingDescription": "In December 2020, 81,578 referrals into IAPT services in England started a course of treatment."
            },
            {
                "observedNode": "Event",
                "measuredValue": 48331,
                "measuredProperty": "COUNT",
                "observationDate": "2021-02-25",
                "disambiguatingDescription": "In December 2020, 48,331 referrals into IAPT services in England completed a course of treatment."
            }
        ],
        "structuralMetadata": {
            "tables": [
                {
                    "name": "IAPT.iapt.Rep_Referral",
                    "description": "IAPT.iapt.Rep_Referral",
                    "columns": [
                        {
                            "name": "Count of number of Non-guided Self Help (Computer) sessions (derived)",
                            "description": "Count of number of Non-guided Self Help (Computer) sessions (derived)",
                            "dataType": "Number",
                            "sensitive": false,
                            "values": null
                        }
                    ]
                },
                {
                    "name": "IAPT.iapt.Rep_Referral",
                    "description": "IAPT.iapt.Rep_Referral",
                    "columns": [
                        {
                            "name": "Pseudonymised Service Request Identifier",
                            "description": "A request for the provision of care services to a PATIENT.",
                            "dataType": "String",
                            "sensitive": false,
                            "values": null
                        }
                    ]
                }
            ],
            "syntheticDataWebLink": null
        }
    }

    ```

### BioSchema

This example payload (`{"metadata":<json>}`) will validate (return status `200`) against TRASER (translation service) endpoint:

`/validate?input_schema=SchemaOrg&input_version=BioSchema`

If you were to use the endpoint `find?with_errors=0` you would also see the following message, showing that this is a valid BioSchema

```json

[
    {
        "name": "HDRUK",
        "version": "2.1.2",
        "matches": false
    },
   ...
    {
        "name": "SchemaOrg",
        "version": "default",
        "matches": false
    },
    {
        "name": "SchemaOrg",
        "version": "BioSchema",
        "matches": true
    },
    {
        "name": "SchemaOrg",
        "version": "GoogleRecommended",
        "matches": false
    }
]

```

??? example "NHS England: Cancer Registration Data"

    ```json
    {
        "@context": "https://schema.org/",
        "@id": "https://hdruk.ac.uk",
        "@type": "Dataset",
        "identifier": [
            "5124f2"
        ],
        "version": "2.0.0",
        "url": "https://hdruk.ac.uk/1234",
        "name": "Cancer Registration Data",
        "alternateName": "Cancer Registration Data",
        "description": "The National Cancer Registration and Analysis Service (NCRAS) at Public Health England supplies cancer registration data to NHS Digital. This data is available to be linked to other data held by NHS Digital in order to provide notifications on an individual's cancer status, be available to support research studies and to identify potential research participants for clinical trials.\n\nNCRAS is the population-based cancer registry for England. It collects, quality assures and analyses data on all people living in England who are diagnosed with malignant and pre-malignant neoplasms, with national coverage since 1971.\n\nThe Cancer Registration dataset comprises England data to the present day, and Welsh data up to April 2017.\n\nTimescales for dissemination of agreed data can be found under 'Our Service Levels' at the following link: [https://digital.nhs.uk/services/data-access-request-service-dars/data-access-request-service-dars-process](https://digital.nhs.uk/services/data-access-request-service-dars/data-access-request-service-dars-process) [Standard response](https://web.www.healthdatagateway.org/dataset/2ed7bbbc-80db-46c2-a45b-632dda40794b)",
        "citation": "",
        "creator": {
            "@type": "Organization",
            "legalName": "NHS ENGLAND",
            "name": "NHS ENGLAND",
            "email": "england.contactus@nhs.net",
            "description": "",
            "identifier": "",
            "sameAs": null
        },
        "maintainer": {
            "@type": "Organization",
            "legalName": "NHS England (NHSE)",
            "name": "NHS England (NHSE)",
            "email": "england.contactus@nhs.net",
            "description": "",
            "identifier": "",
            "sameAs": null
        },
        "publisher": {
            "@type": "Organization",
            "legalName": "NHS ENGLAND",
            "name": "NHS ENGLAND",
            "identifier": "https://web.www.healthdatagateway.org/6427fbf67a",
            "description": "",
            "sameAs": null,
            "email": null
        },
        "isAccessibleForFree": false,
        "dateCreated": "2023-06-17T00:00:00.000Z",
        "distribution": {
            "@type": "DataDownload",
            "name": "Once your DARS application has been approved, data will be made available by secure file transfer.\n\nhttps://digital.nhs.uk/services/transfer-data-securely",
            "contentUrl": "https://somehwere.com",
            "encodingFormat": "Unknown"
        },
        "keywords": "Cancer Type, Cancer Behaviour, Cancer Anniversary, Cancer Site, cancer registra",
        "license": "https://digital.nhs.uk/services/data-access-request-service-dars",
        "includedInDataCatalog": null,
        "isBasedOn": null,
        "isPartOf": null,
        "hasPart": null,
        "measurementTechnique": "",
        "sameAs": null,
        "variableMeasured": "",
        "dateModified": null,
        "datePublished": null,
        "dct:conformsTo": {
            "http://purl.org/dc/terms/conformsTo": {
                "@id": "https://bioschemas.org/profiles/Dataset/1.1-DRAFT",
                "@type": "CreativeWork"
            }
        }
    }
    ```
