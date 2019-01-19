import requests

# method to make api calls to pagerduty
def get_incidents(**kwargs):
	since = kwargs.get("since")
	until = kwargs.get("until")
	team_id = kwargs.get("team_id")
	urgencies = kwargs.get("urgency", "high")
	api_key = kwargs.get("api_key")

	URL = "https://api.pagerduty.com/incidents"

	headers = {
		"Authorization": "Token token={}".format(api_key),
        "Accept": "application/vnd.pagerduty+json;version=2"
	}

	# create payload
	payload = {
		"since": since,
		"until": until,
		"team_ids[]": team_id,
		"urgencies[]": urgencies,
		"limit": 100,
		"time_zone": "UTC"
	}

	incidents = []
	response_length = 100
	count = 0

	# get all the incidents in batches of 100
	while True:
		payload["offset"] = count * response_length
		response = requests.request("GET", URL, headers=headers, params=payload)
		json_obj = response.json()

		current_incidents = json_obj.get("incidents")
		if len(current_incidents) != 0:
			incidents += current_incidents
		else:
			break

		count += 1

	return incidents


if __name__ == "__main__":
	call_pd(since="17-01-2019", until="19-01-2019", team_id="PAE6H7O", api_key="")





