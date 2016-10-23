$(function(){
    var audio = document.getElementById('audio-streaming');
    var video = document.getElementById('video');
    //video.play();

    $('.stream a').click(function(e){
        e.preventDefault();
        video.setAttribute('src', $(this).attr('href'));
        video.play();
    });
    
    $('.audio-wrapper a').click(function(e){
            e.preventDefault();
            $("#audio-streaming").attr('src', $(this).parent().attr('id'));
            $("#audio-screen img").attr('src', ($(this).find('img').attr('src')));
            audio.play();
    });

});
