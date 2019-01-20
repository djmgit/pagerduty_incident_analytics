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

	$scope.fetch = function() {
		
	}


	$scope.init();
	

 

});




