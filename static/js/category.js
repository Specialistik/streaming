$(function(){
    $('.pic-wrapper').hover(function() {
        console.log('tesxt');
        $( this ).find('.cat-desc').show();
    }, function() {
        $('.cat-desc').hide();
    });
});