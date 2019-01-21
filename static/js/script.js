// Iniialise app and controller
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
	$scope.showData = false;
	$scope.loader = false;

	$scope.click = function() {
		console.log($scope.team);
	}

	$scope.init = function() {

		$http.get("/api/v1/teams").then(function(response) {
			$scope.teams = response.data.teams;
			console.log($scope.teams);
		})
	}

	$scope.getTeam = function(team_id) {
		for (var index = 0; index < $scope.teams.length; index++) {
			if ($scope.teams[index].id == team_id) {
				
				return $scope.teams[index]
			}
		}
	}

	$scope.visualize = function(incident_frequencies) {
		pie_data = []

		for (var index = 0; index < incident_frequencies.length; index++) {
			incident = incident_frequencies[index];
			pie_data.push({
				"name": incident.incident_name,
				"y": parseInt(incident.incident_frequency)
			})
		}

		console.log(pie_data);

		//pie_data[0].sliced = true;
		//pie_data[0].selected = true;

		Highcharts.chart('pie', {
    		chart: {
        		plotBackgroundColor: null,
        		plotBorderWidth: null,
        		plotShadow: false,
        		type: 'pie'
    		},
    		title: {
        		text: 'Incident frequencies'
    		},
    		tooltip: {
        		pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    		},
    		plotOptions: {
        		pie: {
            		allowPointSelect: true,
            		cursor: 'pointer',
            		dataLabels: {
                		enabled: false
            		},
            		showInLegend: false
        		}
    		},
    		series: [{
        		name: 'Incidents',
        		colorByPoint: true,
        		data: pie_data
    		}]
    	});
	}

	$scope.fetch = function() {
		var team = $scope.getTeam($scope.team);
		$scope.loader = true;
		$http.get("/api/v1/incident_analytics?since=" + $scope.since + "&until=" + $scope.until + "&team_id=" + team.id + "&team=" + team.name + "&urgency=" + $scope.urgency).then(function(response) {
			console.log(response.data);
			$scope.incident_frequencies = response.data.incident_frequencies;
			$scope.limit = parseInt($scope.limit)

			if ($scope.limit !== "" && $scope.limit !== undefined && $scope.limit < $scope.incident_frequencies.length) {
				$scope.incident_frequencies = $scope.incident_frequencies.slice(0, $scope.limit)
			}
			$scope.visualize($scope.incident_frequencies)
			$scope.showData = true;
			$scope.loader = false;
		});
	}


	$scope.init();

});




