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
			username: " introdueix un nom d'usuari",
			password: " introdueix una contrasenya",
			repeatPassword: {
				required: " introdueix una contrasenya",
				equalTo: " les contrasenyes han de ser iguals"
			},
			email: " introdueix un correu electrònic"
		}
	});
});