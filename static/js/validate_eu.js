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
			username: " sartu zure erabiltzaile izena",
			password: " sartu zure pasahitza",
			repeatPassword: {
				required: " sartu zure pasahitza",
				equalTo: " pasahitzak berdinak izan behar dute"
			},
			email: " "
		}
	});
});