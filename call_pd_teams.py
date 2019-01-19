import requests
import configparser

def get_teams(**kwargs):
	api_key = kwargs.get("api_key")
	URL = "https://api.pagerduty.com/teams"

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

		current_teams = json_obj["teams"]
		if len(current_teams) != 0:
			teams += current_teams
		else:
			print ("done")
			break

	return teams

if __name__ == "__main__":
	config = configparser.ConfigParser()
	config.read('appconfig.conf')
	print(len(get_teams(api_key=config["CM"]["API_KEY"])))



