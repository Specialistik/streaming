$(function(){
    $('.pic-wrapper a').click(function(e){
    
        var that = this;
        e.preventDefault();
        console.log($('#video'));
		$('source').attr("src", $(that).attr('href'));
        $('video').play();
    });
    
    $('.multiple-items').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3
    });
});
