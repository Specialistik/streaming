$(function(){
	$('video').play();
    //myVideo.play();

    $('.pic_wrapper a').click(function(e){
        var that = this;
        e.preventDefault();
        console.log($('#video'));
		$('source').attr("src", $(that).attr('href'));
        $('video').play();
    });

	$('#main-cat').click(function(){
        console.log("main cat clicked");
	});
});
