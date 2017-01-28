var animaApp = angular.module('animaApp', [])
animaApp.controller('videoController', function($scope, $http){
	$http.get('/videos_default').then(function (response) {
		console.log(response)
        $scope.video_thumbnails = response.data.thumbnails;
        $scope.$digest();
        $('.jcarousel').jcarousel({vertical: true});
    });
});
