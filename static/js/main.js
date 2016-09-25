$(function(){
    var myPlayer;
    videojs("video").ready(function(){
        myPlayer = this;
        //myPlayer.play();
    });

    $('.pic_wrapper a').click(function(e){
        var that = this;
        e.preventDefault();
        myPlayer.src({"src": $(that).attr('href')}).play();
    });

    // Buttons
	var playButton = $('#play-pause'); //document.getElementById("play-pause");
	var muteButton = $('#mute'); //document.getElementById("mute");
	var fullScreenButton = $("#full-screen");

	// Sliders
	var seekBar = $("#seek-bar");
	var volumeBar = $("#volume-bar");

	// Event listener for the play/pause button
	playButton.click(function() {
		if (myPlayer.paused == true) {
			// Play the video
			myPlayer.play();

			// Update the button text to 'Pause'
			playButton.innerHTML = "Pause";
		} else {
			// Pause the video
			myPlayer.pause();

			// Update the button text to 'Play'
			playButton.innerHTML = "Play";
		}
	});


	// Event listener for the mute button
	muteButton.click(function() {
		if (myPlayer.muted == false) {
			// Mute the video
			myPlayer.muted = true;

			// Update the button text
			muteButton.innerHTML = "Unmute";
		} else {
			// Unmute the video
			myPlayer.muted = false;

			// Update the button text
			muteButton.innerHTML = "Mute";
		}
	});


	// Event listener for the full-screen button
	fullScreenButton.click(function() {
		if (myPlayer.requestFullscreen) {
			myPlayer.requestFullscreen();
		} else if (myPlayer.mozRequestFullScreen) {
			myPlayer.mozRequestFullScreen(); // Firefox
		} else if (myPlayer.webkitRequestFullscreen) {
			myPlayer.webkitRequestFullscreen(); // Chrome and Safari
		}
	});
});
