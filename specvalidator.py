import json
from pathlib import Path
import requests
from openapi_core import OpenAPI, Config
from openapi_core.contrib.requests import RequestsOpenAPIRequest


config = Config(
    spec_validator_cls=None,
)
openapi = OpenAPI.from_file_path('./2024-02-15-preview.json', config=config)

# Load the JSON body from a local file
json_body_path = Path("./input.json")
json_body = json.loads(json_body_path.read_text())

# Create a POST request
url = "https://localhost:3000/openai/deployments/mydeployment/chat/completions"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

request = requests.Request(
    method="POST",
    url=url,
    headers=headers,
    json=json_body
)
openapi_request = RequestsOpenAPIRequest(request.prepare())
result = openapi.unmarshal_request(openapi_request) #breaks on this line
print(result)
