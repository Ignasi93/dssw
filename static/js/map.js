window.onload = function () {
	$ ( "#send" ).click ( function () {
		if ( $ ( "#address" ).val () != "" ) {
			search ( $ ( "#address" ).val () );
		}
	});
	$ ( "body" ).show ();
}

function search ( address ) {
	address = address.replace(/á/g,"a").replace(/à/g,"a").replace(/é/g,"e").replace(/è/g,"e").replace(/í/g,"i").replace(/ó/g,"o").replace(/ò/g,"o").replace(/ú/g,"u");
	$.ajax ( "/mapa?address=" + address, {
		"type" : "post", "success": function ( result ) {
			var resultat = result.split ( '@@@@@' );
			$ ( "#my_div" ).html ( resultat[0] );
			eval ( resultat[1] );
		},
		"beforeSend": function () {
			$ ( "#my_div" ).html ( "" );
			$ ( "#map" ).html ( "" );
		},
		"async" : true,
	})
}