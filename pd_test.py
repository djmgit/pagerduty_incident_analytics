import requests
import json

def main():
    headers = {
        "Authorization": "Token token=RyxhPFNFfzsYnjsY4G-R",
        "Accept": "application/vnd.pagerduty+json;version=2"
    }

    url = "https://api.pagerduty.com/incidents"

    payload = {
        "since": "18-01-2019",
        "until": "19-01-2019",
        "team_ids[]": "PAE6H7O",
        "urgencies[]": "high",
        "time_zone": "UTC",
        "limit": "1",
        "offset": "89"
    }

    r = requests.request("GET", url, headers=headers, params=payload)
    r = r.json()

    print (len(r.get("incidents")))

    for incident in r.get("incidents"):
        print (incident.get("title"))

    for incident in r.get("incidents"):
        print (incident.get("teams")[0].get("summary"))

if __name__ == "__main__":
    main()
