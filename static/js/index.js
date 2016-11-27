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

    $('#exit').click(function(){
	location.href = '/admin/logout';
    });
});
