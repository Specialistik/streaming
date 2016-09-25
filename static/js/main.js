$(function(){
	//var subcategory = $('.subcategory-tree');
	//$('.subcategory-tree').remove();
	var myVideo = document.getElementById("video");

    $('.pic_wrapper a').click(function(e){
        var that = this;
        e.preventDefault();
		$('#video').attr("src", $(that).attr('href'));//.play();
		myVideo.play();
       // $('#video').src({"src": $(that).attr('href')}).play();
    });

	$('#main-cat').click(function(){

	});

/*	$('#play-pause').click(function() {
		if (myPlayer.paused == true) {
			myPlayer.play();
			$(this).innerHTML = "Pause";
		} else {
			myPlayer.stop();
			$(this).innerHTML = "Play";
		}
	});

	$("#full-screen").click(function() {
		if (myPlayer.requestFullscreen) {
			myPlayer.requestFullscreen();
		} else if (myPlayer.mozRequestFullScreen) {
			myPlayer.mozRequestFullScreen(); // Firefox
		} else if (myPlayer.webkitRequestFullscreen) {
			myPlayer.webkitRequestFullscreen(); // Chrome and Safari
		}
	});*/
/*
    $("#video").addEventListener("timeupdate", function() {
		var value = (100 / myPlayer.duration) * myPlayer.currentTime;
		$("#seek-bar").value = value;
	});*/
/*
	$("#seek-bar").mousedown(function() {
		myPlayer.stop();
	}).mouseup(function() {
		myPlayer.play();
	});*/

	//$('#video').play;

/*	seekBar.addEventListener("mouseup", function() {
		myPlayer.play();
	});*/

/*	$('#volume-bar').addEventListener("change", function() {
		$('#video').volume = volumeBar.value;
	});*/
});
