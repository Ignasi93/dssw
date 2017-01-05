function validateAjax ( language ) {
	var XMLHttpRequestObject = new XMLHttpRequest ();
	var correu = document.getElementById ( "email" );
	var resposta = "";
	var response;
	var params = "?emailV=" + correu.value;

	if ( language == "ca" )
		resposta = "Correu vàlid";
	else if ( language == "en" )
		resposta = "Valid email";
	else if ( language == "es" )
		resposta = "Correo válido";
	else if ( language = "eu" )
		resposta = "Email zuzena";

	if ( XMLHttpRequestObject ) {
		XMLHttpRequestObject.onreadystatechange = function () {
			if ( XMLHttpRequestObject.readyState == 4 ) {
				response = XMLHttpRequestObject.responseText;
				if ( response == "" ) {
					document.getElementById ( "validEM" ).innerHTML = resposta;
					console.log("Valid: " + document.getElementById ( "validEM" ).value);
					document.getElementById ( "errorEM" ).innerHTML = "";
					console.log("Buit: " + document.getElementById ( "errorEM" ).value );
				} else {
					document.getElementById ( "validEM" ).innerHTML = "";
					console.log("no hauria d'entrar " + document.getElementById ( "validEM" ).value);
					document.getElementById ( "errorEM" ).innerHTML = response;
					console.log("no hauria d'entrar " + document.getElementById ( "errorEM" ).value);
				}
			}
		}
	} // tanca l'if

	XMLHttpRequestObject.open ( "get", "/validar/" + params, true );
	XMLHttpRequestObject.send ( null );
}