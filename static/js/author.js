$(function(){
	$('#video').play();

    $('.pic-wrapper a').click(function(e){
        var that = this;
        e.preventDefault();
        console.log($('#video'));
		$('source').attr("src", $(that).attr('href'));
        $('video').play();
    });
    
    $('.audio-img').click(function(e) {
        var that = this;
        e.preventDefault();
        console.log($(this).parent().attr('id'));
    });
});
