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
			username: " introduce un nombre de usuario",
			password: " introduce una contraseña",
			repeatPassword: {
				required: " introduce una contraseña",
				equalTo: " las contraseñas tienen que ser iguales"
			},
			email: " introduce un correo electrónico"
		}
	});
});