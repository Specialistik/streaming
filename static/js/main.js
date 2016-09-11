$(function(){
    //$('.carousel').carousel('pause');
    $('.video').click(function(){this.paused?this.play():this.pause();});

    if (window.chrome)
    $("[type=video\\\/mp4]").each(function()
    {
        $(this).attr('src', $(this).attr('src').replace(".mp4", "_c.mp4"));
    });
});
