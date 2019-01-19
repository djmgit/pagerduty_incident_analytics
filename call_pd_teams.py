import requests

def get_teams(**kwargs):
	api_key = kwargs.get("api_key")
	URL = "https://api.pagerduty.com/incidents"

	headers = {
		"Authorization": "Token token={}".format(api_key),
        "Accept": "application/vnd.pagerduty+json;version=2"
	}

	payload = {
		"limit": 100
	}

	teams = []
	count = 0
	respose_length = 100

	# get all teams
	while True:
		payload["offset"] = count * respose_length

		response = requests.request("GET", URL, headers=headers, params=payload)
		json_obj = response.json()

		
