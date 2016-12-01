$(function(){
    var audio = document.getElementById('audio-streaming');
    var video = document.getElementById('video');
    //video.play();

    $('.stream a').click(function(e){
        e.preventDefault();
        video.setAttribute('src', $(this).attr('href'));
        video.play();
    });
});
