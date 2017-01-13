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
    
    $('#cabinet').click(function(){
	    $('.user-info').toggle();
    });

    $('#profile').click(function(){
		location.href = '/profile';
    });

    $('#account').click(function(){
		location.href = '/account';
    });

	$("#register-oldschool").click(function(){
		$("#register-oldschool").attr("disabled", true);
		$.ajax({
			type: "POST",
			url: "/register",
			data: $('#register-form').serialize(),
			success: function(msg){
				alert(msg);
				location.reload()
			},
			error: function(msg){
				alert("Не удалось зарегистрироваться");
			}
		}).done(function() {
			$("#register-oldschool").attr("disabled", false);
		};
	});
});
