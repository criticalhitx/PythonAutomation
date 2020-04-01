## This code is to list name of Tenant in JSON formatted text
## request link : https://sandboxapicdc.cisco.com/api/class/fvTenant.json using postman
import json

with open('response_tenant_sandbox.json', 'r') as f:
    loadedJSON= json.load(f)

que = loadedJSON.get('imdata')

tenantInput = input("Please Enter a Tenant to proceed :")

for m in que: #i is dictionary also (baris 4)
    if m['fvTenant']['attributes']['name'] == tenantInput:
    	print("Listing Attributes of Tenant = "+tenantInput)
    	print("annotation = "+ m['fvTenant']['attributes']['annotation'])
    	print("childAction = "+ m['fvTenant']['attributes']['childAction'])
    	print("descr = "+ m['fvTenant']['attributes']['descr'])
    	print("dn = "+ m['fvTenant']['attributes']['dn'])
    	print("extMngdBy = "+ m['fvTenant']['attributes']['extMngdBy'])
    	print("lcOwn = "+ m['fvTenant']['attributes']['lcOwn'])
    	print("modTs = "+ m['fvTenant']['attributes']['modTs'])
    	print("monPolDn = "+ m['fvTenant']['attributes']['monPolDn'])
    	print("name = "+ m['fvTenant']['attributes']['name'])
    	print("nameAlias = "+ m['fvTenant']['attributes']['nameAlias'])
    	print("ownerKey = "+ m['fvTenant']['attributes']['ownerKey'])
    	print("ownerTag = "+ m['fvTenant']['attributes']['ownerTag'])
    	break
	#if att['descr'] == "Tenant by REB":
	#	Resp = att['dn']
	#	break
#print(Resp)