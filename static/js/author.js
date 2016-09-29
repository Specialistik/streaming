$(function(){
	var myVideo = document.getElementById("video").play();

    $('.pic_wrapper a').click(function(e){
        var that = this;
        e.preventDefault();
		myVideo.attr("src", $(that).attr('href')).play();
    });

	$('#main-cat').click(function(){
        console.log("main cat clicked");
	});
});
