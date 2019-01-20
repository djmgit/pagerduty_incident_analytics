from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_cors import CORS
from pd_core import get_incident_frequency, get_all_teams
import json
import re
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "THIS IS SECRET"
CORS(app)
path = os.path.dirname(os.path.abspath(__file__))

@app.route("/api/v1/teams")
def get_teams():
	all_teams = get_all_teams()

	response = {
		"status": "OK",
		"teams_count": len(all_teams),
		"teams": all_teams
	}

	return jsonify(response)

@app.route("/api/v1/incident_analytics")
def incident_analytics():
	since = request.args.get("since")
	until = request.args.get("until")
	team = request.args.get("team")
	team_id = request.args.get("team_id")
	urgency = request.args.get("urgency", "high")

	response = get_incident_frequency(since=since, until=until, team=team, team_id=team_id, urgency=urgency)

	return jsonify(response)

# serve the app root
@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
