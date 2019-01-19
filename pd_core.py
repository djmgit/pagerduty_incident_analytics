from call_pd_teams import get_teams
from call_pd_incident import get_incidents
import configparser

config = configparser.ConfigParser()
config.read('appconfig.conf')

def get_incident_frequency(**kwargs):
	since = kwargs.get("since")
	until = kwargs.get("until")
	team = kwargs.get("team")
	team_id = kwargs.get("team_id")
	urgencies = kwargs.get("urgency", "high")

	api_key = config["API"]["API_KEY"]

	incidents = get_incidents(since=since, until=until, team_id=team_id, urgencies=urgencies, api_key=api_key)
	incident_frequency = {}
	incident_ids = {}

	for incident in incidents:
		title = incident.get("title")
		incident_frequency[title] = incident_frequency.get(title, 0) + 1
		if not incident_ids.get(title):
			incident_ids[title] = incident.get("id")

	incident_frequency_list = []

	for incident in incident_frequency:
		incident_frequency_list.append({
			"incident_name": incident,
			"incident_id": incident_ids.get(incident),
			"incident_frequency": incident_frequency[incident]
		})

	incident_frequency_list.sort(key=lambda x:x.get("incident_frequency"))
	incident_frequency_list.reverse()

	response = {
		"status": "OK",
		"unique_incident_count": len(incident_frequency_list),
		"incident_frequencies": incident_frequency_list,
		"since": since,
		"until": until,
		"urgency": urgencies,
		"team": team
	}

	return response

def get_all_teams():
	api_key = config["API"]["API_KEY"]
	return get_teams(api_key=api_key)

if __name__ == "__main__":
	#r = get_incident_frequency(since="18-01-2019", until="19-01-2019", team="CM", team_id='PAE6H7O')
	#print ("\n")
	#print (r["incident_frequencies"][0])
	#print ("\n")
	#print (r["incident_frequencies"][1])

	get_all_teams()
