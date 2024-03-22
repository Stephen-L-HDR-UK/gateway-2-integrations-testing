import requests
import json
import glob

metadata = {}
for file in glob.glob("data/*/*/*.json"):
    _, model, version, fname = file.split("/")
    fname = fname.split(".json")[0]
    if model not in metadata:
        metadata[model] = {}
    if version not in metadata[model]:
        metadata[model][version] = {}

    metadata[model][version][fname] = json.load(open(file))


traser_uri = "http://localhost:3001/"
headers = {
    "Content-Type": "application/json",
}
extra = {
    "id": "placeholder",
    "pid": "placeholder",
    "datasetType": "Healthdata",
    "publisherId": "123",
    "publisherName": "Tst Test",
}


def translate(input_model, input_version, output_model, output_version, metadata):

    response = requests.post(
        f"{traser_uri}translate?input_schema={input_model}&input_version={input_version}&output_schema={output_model}&output_version={output_version}",
        headers=headers,
        json={"metadata": metadata, "extra": extra},
    )
    return response.status_code, response.json()


for model, versions in metadata.items():
    for version, metadatas in versions.items():
        for name, metadata in metadatas.items():
            for output_model, output_version in [
                ["GWDM", "1.0"],
                ["GWDM", "1.1"],
                ["GWDM", "1.2"],
            ]:
                code, output = translate(
                    model, version, output_model, output_version, metadata
                )
                print(model, version, name, code)
                if code != 200:
                    print(json.dumps(output, indent=6))
                    exit(0)
