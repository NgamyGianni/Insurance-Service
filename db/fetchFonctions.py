import requests

def fetchFacilityByFacilityId(facilityId):
	url = ""
	request = requests.get(url)
	json = request.json()

	return [element for element in json if element["id"] == facilityId][0]

