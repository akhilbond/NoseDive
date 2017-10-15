$(document).ready(function(){
	var usernameLogIn
	var passwordSignIn
	var usernameSignUp
	var firstName
	var lastName
	var passwordSignUp
	var facebookURL
	var	twitterURL
	var instagramURL
	var phoneNumber
	var userInfo = {}
	var image

	// immediately invoked function expression
	$(function() {
	  $('#login-form-link').click(function(e) {
			$("#login-form").delay(100).fadeIn(100);
	 		$("#register-form").fadeOut(100);
			$('#register-form-link').removeClass('active');
			$(this).addClass('active');
			e.preventDefault();
		});

		$('#register-form-link').click(function(e) {	
			$("#register-form").delay(100).fadeIn(100);
	 		$("#login-form").fadeOut(100);
			$('#login-form-link').removeClass('active');
			$(this).addClass('active');
			e.preventDefault();
		});
	});


	$('#login-submit').on('click', function(){
		event.preventDefault()
		usernameLogIn = $('#usernameLogIn').val()
		passwordSignIn = $('#passwordLogIn').val()

		console.log(usernameLogIn)
		console.log(passwordSignIn)

		window.location.href = '/loggedIn.html'

		// $.ajax({
		// 	method: "GET",
		// 	url: "/loggedin"
		// }).done(function(response){
		// 	console.log("response")
		// 	window.location.href = '/loggedIn.html'
		// })
	});

    $("#uploadSubmit").submit(function (event) {
        //disable the default form submission
        event.preventDefault();
        //grab all form data  
        var formData = $(this).serialize();

        $.ajax({
            url: 'upload',
            type: 'POST',
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
            success: function () {
                alert('Form Submitted!');
            },
            error: function(){
                alert("error in ajax form submission");
            }
        });

        return false;
    });


	$("#register-submit").on('click', function(){
		event.preventDefault()

		usernameSignUp = $("#usernameSignUp").val()
		firstName = $("#firstName").val()
		lastName = $("#lastName").val()
		passwordSignUp = $("#passwordSignUp").val()
		facebookURL = $("#facebook-url").val()
		twitterURL = $("#twitter-url").val()
		instagramURL = $("#instagram-url").val()
		phoneNumber = $("#phone-number").val()

		userInfo = {firstName, phoneNumber, facebookURL, twitterURL, instagramURL}
		// console.log(userInfo)
		console.log(image)

		$.ajax({
			method: "POST",
			url: "/register",
			data: userInfo
		}).done(function(response){
			console.log(response)
		})
	})

});//end document.ready

