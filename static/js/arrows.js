$(function(){
    $('.arrow').click(function(e){
        var that = this;
        e.preventDefault();
        $( "body" ).fadeOut( "slow", function() {
            if (window.location.pathname == '/') {
                location.href = $(that).find('a').attr('href');
            } else location.href = '/';
        });
    });
    
    $('.arrow-left').hover(function() {
        $(this).find('img').attr('src', "/static/images/arrow_left_hover.png");
    }, function() {
        $(this).find('img').attr('src', "/static/images/arrow_left.png");
    });
    
    $('.arrow-right').hover(function() {
        $(this).find('img').attr('src', "/static/images/arrow_right_hover.png");
    }, function() {
        $(this).find('img').attr('src', "/static/images/arrow_right.png");
    });
});
