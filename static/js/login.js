function onSignIn ( user ) {
	var profile = user.getBasicProfile ();
	$ ( "#login" ).hide ();
	$ ( "#logout" ).html ( "<div style='float:right; padding:10px;'><b> Hello " + profile.getName() +
	"</b><br/>" + "<a href='#' onclick='logout();'>Logout</a></div>" );
	$ ( "#logout" ).show ();
}

function logout () {
	var auth2 = gapi.auth2.getAuthInstance();
	auth2.signOut().then ( function () {
		$ ( "#logout" ).hide ();
		$ ( "#logout" ).html ( "" );
		$ ( "#login" ).show ();
	});
}