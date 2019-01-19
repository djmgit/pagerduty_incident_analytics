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

	api_key = config[team]["API_KEY"]

	incidents = get_incidents(since=since, until=until, team_id=team_id, urgencies=urgencies, api_key=api_key)

	incident_frequency = {}

	for incident in incidents:
		title = incident.get("title")
		incident_frequency[title] = incident_frequency.get(title, 0) + 1

	incident_frequency_list = []

	for incident in incident_frequency:
		incident_frequency_list.append({
			"incident_name": incident,
			"incident_frequency": incident_frequency[incident]
		})

	response = {
		"unique_incident_count": len(incident_frequency_list),
		"incident_frequency": incident_frequency_list,
		"since": since,
		"until": until,
		"urgency": urgencies,
		"team": team
	}

	return response

if __name__ == "__main__":
	pass
