jQuery ( function ( $ ) {
	$("#formulario").validate({
		rules : {
			username: "required",
			password: "required",
			repeatPassword: {
				equalTo: '#password'
			},
			email: {
				required: true,
				email: true
			}
		},

		messages: {
			username: " put an username",
			password: " put a password",
			repeatPassword: {
				required: " put a password",
				equalTo: " passwords must be equals"
			},
			email: " put an e-mail"
		}
	});
});