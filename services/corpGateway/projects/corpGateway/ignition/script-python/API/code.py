bypassCertValidation=True
SECRETSPROVIDER="SiteSecrets"

def getSecret(gatewayName=None):
	secret=system.secrets.readSecretValue(SECRETSPROVIDER, gatewayName)
	return secret.getSecretAsString()
	
def getHeaders(gatewayName):
	APIKEY=getSecret(gatewayName)
	return {'X-Ignition-API-Token': APIKEY}

def getBASEURL(gatewayName, baseURL='http://{}:8088'):
	return baseURL.format(gatewayName.lower())

def apiGet(endpoint, gatewayName, baseURL='http://{}:8088'):
	url = endpoint.format(baseUrl=API.getBASEURL(gatewayName, baseURL))
	headers=API.getHeaders(gatewayName)
	client = system.net.httpClient(bypass_cert_validation=bypassCertValidation)
	
	response = client.get(url, headers=headers)	
	
	return response

def apiPut(endpoint, payload, gatewayName, baseURL='http://{}:8088'):
	client = system.net.httpClient(bypass_cert_validation=bypassCertValidation)
	headers=getHeaders(gatewayName)
	headers['Content-Type']= 'application/json'
	url=endpoint.format(baseUrl=API.getBASEURL(gatewayName, baseURL))
#	return url
	try:
		# 4. Send the POST request
		jsonPayload = system.util.jsonEncode(payload)
		response = client.put(url, data=jsonPayload, headers=headers)
		
		# 5. Process the response
		if response.good:
#			return "Request succeeded (%d)" % response.statusCode
		# Parse JSON response body into a Python dict/list
			responseData = response.json
			msg= "Server response:", responseData
		else:
			msg= "Request failed (%d)" % response.statusCode
	
	except Exception as e:
		msg= "Error executing HTTP POST:", e
	return msg


def MQTTtransmissionState(gatewayName, baseURL='http://{}:8088'):
	endpoint='{baseUrl}/data/api/v1/resources/singleton/com.cirruslink.mqtt.transmission.gateway/general'
	response= API.apiGet(endpoint, gatewayName, baseURL)
	return response

def MQTTtransmissionToggle(payload, gatewayName, baseURL='http://{}:8088'):
	endpoint='{baseUrl}/data/api/v1/resources/com.cirruslink.mqtt.transmission.gateway/general'
	response= API.apiPut(endpoint, payload, gatewayName, baseURL)
	return response