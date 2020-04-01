## This code is to list only tenant info
## request link : https://sandboxapicdc.cisco.com/api/class/fvTenant.json using postman
import json

with open('response_tenant_sandbox.json', 'r') as f:
    loadedJSON= json.load(f)

print(json.dumps(loadedJSON, indent=4, sort_keys=True))