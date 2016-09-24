$(function(){
    var myPlayer;
    videojs("main_video").ready(function(){
        myPlayer = this;
        myPlayer.play();
    });

    $('.pic_wrapper a').click(function(e){
        var that = this;
        e.preventDefault();
        myPlayer.src({"src": $(that).attr('href')}).play();
    });
});
