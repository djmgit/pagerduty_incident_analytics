// Iniialise app and controller
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
	
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

	$scope.fetch = function() {
		var team = $scope.getTeam($scope.team);
		$http.get("/api/v1/incident_analytics?since=" + $scope.since + "&until=" + $scope.until + "&team_id=" + team.id + "&team=" + team.name + "&urgency=" + $scope.urgency).then(function(response) {
			console.log(response)
		});
	}


	$scope.init();
	

 

});




