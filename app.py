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

@app.route("/api/v1/get_teams")
def get_teams():
	all_teams = get_all_teams()

	response = {
		"status": "OK",
		"teams_count": len(all_teams),
		"teams": all_teams
	}

	return jsonify(response)
