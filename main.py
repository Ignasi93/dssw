#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import urllib
import re
import json
from webapp2_extras import sessions
import session_module
from google.appengine.ext.webapp \
	import template
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

myconfig_dict = {}
myconfig_dict[ 'webapp2_extras.sessions' ] = {
	'secret_key' : 'my-super-secret-key-somemorearbitarythingstosay',
}

class Usuari ( ndb.Model ) :
	nom = ndb.StringProperty ( required = True )
	contrasenya = ndb.StringProperty ( required = True )
	correu = ndb.StringProperty ( required = True )
	data = ndb.DateTimeProperty ( auto_now_add = True )

class Image ( ndb.Model ) :
	user = ndb.StringProperty ()
	public = ndb.BooleanProperty ()
	blob_key = ndb.BlobKeyProperty ()

#**********************************************************************************

class EnglishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'main_en.html', {}  ) )

class SpanishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'main_es.html', {} ) )

class EuskaraHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'main_eu.html', {} ) )

class MainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'main_ca.html', {} ) )

#**********************************************************************************

USERNAME_RE = re.compile ( r"^[a-zA-Z0-9]{3,20}" )
PASSWORD_RE = re.compile ( r"^.{6,15}" )
EMAIL_RE = re.compile ( '(<)?(\w+@\w+(?:\.\w+)+)(?(1)>)' )

# 0 = username; 1 = password; 2 = email
def validate ( field, num ) :
	if num == 0 :
		return USERNAME_RE.match ( field )
	elif num == 1 :
		return PASSWORD_RE.match ( field )
	elif num == 2:
		return EMAIL_RE.match ( field )

def htmlValues ( un, pw, rpw, em, eun, epw, erpw, eem ) :
	return {
		'username': un,
		'password': pw,
		'repeatPassword': rpw,
		'email': em,
		'errorUN': eun,
		'errorPW': epw,
		'errorRPW': erpw,
		'errorEM': eem
	}

class RegisterMainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_ca.html', {} ) )

	def post ( self ) :
		username = self.request.get ( 'username' )
		password = self.request.get ( 'password' )
		repeatPassword = self.request.get ( 'repeatPassword' )
		email = self.request.get ( 'email' )
		errorUN = ""
		errorPW = ""
		errorRPW = ""
		errorEM = ""
		error = False

		if not validate ( username, 0 ) :
			error = True
			errorUN = "El nom d'usuari no pot contindre nombres o s&iacute;mbols"
		if not validate ( password, 1 ) :
			error = True
			errorPW = "La contrasenya ha de ser entre 6 i 15 caracters de llarg&agrave;ria"
		if repeatPassword != password :
			error = True
			errorRPW = "Les contrasenyes han de ser iguals"
		if not validate ( email, 2 ) :
			error = True
			errorEM = "No &eacute;s un correu v&agrave;lid"

		if ( Usuari.query ( Usuari.nom == username ).count () ) == 1 :
			error = True
			errorUN += 'Eixe usuari ja existeix'
		if ( Usuari.query ( Usuari.correu == email ).count () ) == 1 :
			error = True
			errorEM += 'Eixe correu ja existeix'

		if not error:
			user = Usuari (
				nom = username,
				contrasenya = password,
				correu = email
			)
			user.put()
			self.response.out.write ( template.render ( 'register_ca.html', {} ) )
			self.response.write ( '<h2>Formulari rebut</h2>' )
			self.response.write ( "Hola: %s <br>" % self.request.get ( 'username' ) )
		else :
			values = htmlValues ( username, password, repeatPassword, email, errorUN, errorPW, errorRPW, errorEM )
			self.response.out.write ( template.render ( 'register_ca.html', values ) )
			self.response.write ( '<h6>ERROR</h6>' )

class RegisterEnglishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_en.html', {} ) )

	def post ( self ) :
		username = self.request.get ( 'username' )
		password = self.request.get ( 'password' )
		repeatPassword = self.request.get ( 'repeatPassword' )
		email = self.request.get ( 'email' )
		errorUN = ""
		errorPW = ""
		errorRPW = ""
		errorEM = ""
		error = False

		if not validate ( username, 0 ) :
			error = True
			errorUN = "Username can not contain numbers or symbols"
		if not validate ( password, 1 ) :
			error = True
			errorPW = "Password length must be from 6 to 15 characters"
		if repeatPassword != password :
			error = True
			errorRPW = "Passwords must be equals"
		if not validate ( email, 2 ) :
			error = True
			errorEM = "Not an email"

		if ( Usuari.query ( Usuari.nom == username ).count () ) == 1 :
			error = True
			errorUN += 'Username already in use'
		if ( Usuari.query ( Usuari.correu == email ).count () ) == 1 :
			error = True
			errorEM += 'Email already in use'

		if not error:
			user = Usuari (
				nom = username,
				contrasenya = password,
				correu = email
			)
			user.put()
			self.response.out.write ( template.render ( 'register_en.html', {} ) )
			self.response.write ( '<h2>Form received</h2>' )
			self.response.write ( "Hello: %s <br>" % self.request.get ( 'username' ) )
		else :
			values = htmlValues ( username, password, repeatPassword, email, errorUN, errorPW, errorRPW, errorEM )
			self.response.out.write ( template.render ( 'register_en.html', values ) )
			self.response.write ( '<h6>ERROR</h6>' )

class RegisterSpanishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_es.html', {} ) )

	def post ( self ) :
		username = self.request.get ( 'username' )
		password = self.request.get ( 'password' )
		repeatPassword = self.request.get ( 'repeatPassword' )
		email = self.request.get ( 'email' )
		errorUN = ""
		errorPW = ""
		errorRPW = ""
		errorEM = ""
		error = False

		if not validate ( username, 0 ) :
			error = True
			errorUN = "El nombre de usuario no puede contener n&uacute;meros o s&iacute;mbolos"
		if not validate ( password, 1 ) :
			error = True
			errorPW = "La contrase&ntilde;a tiene que ser de entre 6 y 15 car&aacute;cteres de longitud"
		if repeatPassword != password :
			error = True
			errorRPW = "Las contrase&ntilde;as tienen que ser iguales"
		if not validate ( email, 2 ) :
			error = True
			errorEM = "No es un correu v&aacute;lido"

		if ( Usuari.query ( Usuari.nom == username ).count () ) == 1 :
			error = True
			errorUN += 'Nombre de usuario en uso'
		if ( Usuari.query ( Usuari.correu == email ).count () ) == 1 :
			error = True
			errorEM += 'Correo en uso'

		if not error:
			user = Usuari (
				nom = username,
				contrasenya = password,
				correu = email
			)
			user.put()
			self.response.out.write ( template.render ( 'register_es.html', {} ) )
			self.response.write ( '<h2>Formulario recibido</h2>' )
			self.response.write ( "Hola: %s <br>" % self.request.get ( 'username' ) )
		else :
			values = htmlValues ( username, password, repeatPassword, email, errorUN, errorPW, errorRPW, errorEM )
			self.response.out.write ( template.render ( 'register_es.html', values ) )
			self.response.write ( '<h6>ERROR</h6>' )

class RegisterEuskaraHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_eu.html', {} ) )

	def post ( self ) :
		username = self.request.get ( 'username' )
		password = self.request.get ( 'password' )
		repeatPassword = self.request.get ( 'repeatPassword' )
		email = self.request.get ( 'email' )
		errorUN = ""
		errorPW = ""
		errorRPW = ""
		errorEM = ""
		error = False

		if not validate ( username, 0 ) :
			error = True
			errorUN = "erabiltzaileak ez du zenbakirik ezta ikurrik onartzen"
		if not validate ( password, 1 ) :
			error = True
			errorPW = "Pasahitzak 6 eta 15 karaktere arteko luzera izan behar du"
		if repeatPassword != password :
			error = True
			errorRPW = "Pasahitzak berndinak izan behar dira"
		if not validate ( email, 2 ) :
			error = True
			errorEM = "Ez da email-a"

		if ( Usuari.query ( Usuari.nom == username ).count () ) == 1 :
			error = True
			errorUN += 'Erabiltzaile hori erregistratua dago'
		if ( Usuari.query ( Usuari.correu == email ).count () ) == 1 :
			error = True
			errorEM += 'Posta elektroniko hori erregistratua dago'

		if not error:
			user = Usuari (
				nom = username,
				contrasenya = password,
				correu = email
			)
			user.put()
			self.response.out.write ( template.render ( 'register_eu.html', {} ) )
			self.response.write ( '<h2>Formularioa ondo jaso da</h2>' )
			self.response.write ( "Hello: %s <br>" % self.request.get ( 'username' ) )
		else :
			values = htmlValues ( username, password, repeatPassword, email, errorUN, errorPW, errorRPW, errorEM )
			self.response.out.write ( template.render ( 'register_eu.html', values ) )
			self.response.write ( '<h6>ERROR</h6>' )

#**********************************************************************************

class ValidateMainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		error = False
		errorEM = ""
		email = self.request.get ( 'emailV' )
		if not validate ( email, 2 ) :
			error = True
			errorEM = "Not a valid email "
		alreadyInDB = Usuari.query ( Usuari.correu == email ).count ()
		if alreadyInDB >= 1 :
			error = True
			errorEM += "Email already used"
		if not error :
			errorEM = ""
		self.response.write ( errorEM )

#**********************************************************************************

class UsersMainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		usuaris = Usuari.query ()
		self.response.write ( '<h1>Usuaris registrats</h1>' )
		self.response.write ( '<link rel="stylesheet" href="/styles/main.css">' )
		self.response.write ( '<link rel="stylesheet" href="/styles/table.css">' )
		self.response.write ( '''
			<table>
				<tr>
					<th>Nom</th>
					<th>Correu</th>
					<th>Registrat</th>
				</tr>
		''' )
		for current in usuaris.fetch () :
			self.response.write ( ''' 
				<tr>
					<td>''' + current.nom + '''</td>
					<td>''' + current.correu + '''</td>
					<td>''' + str ( current.data ) + '''</td>
					''' )
			self.response.write ( '''</tr>''' )
		self.response.write ( '''</table>''' )

class UsersEnglishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		usuaris = Usuari.query ()
		self.response.write ( '<h1>Registered users</h1>' )
		self.response.write ( '<link rel="stylesheet" href="/styles/main.css">' )
		self.response.write ( '<link rel="stylesheet" href="/styles/table.css">' )
		self.response.write ( '''
			<table>
				<tr>
					<th>Name</th>
					<th>Email</th>
					<th>Registered</th>
				</tr>
		''' )
		for current in usuaris.fetch () :
			self.response.write ( ''' 
				<tr>
					<td>''' + current.nom + '''</td>
					<td>''' + current.correu + '''</td>
					<td>''' + str ( current.data ) + '''</td>
					''' )
			self.response.write ( '''</tr>''' )
		self.response.write ( '''</table>''' )

class UsersSpanishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		usuaris = Usuari.query ()
		self.response.write ( '<h1>Usuarios registrados</h1>' )
		self.response.write ( '<link rel="stylesheet" href="/styles/main.css">' )
		self.response.write ( '<link rel="stylesheet" href="/styles/table.css">' )
		self.response.write ( '''
			<table>
				<tr>
					<th>Nombre</th>
					<th>Correo</th>
					<th>Registrado</th>
				</tr>
		''' )
		for current in usuaris.fetch () :
			self.response.write ( ''' 
				<tr>
					<td>''' + current.nom + '''</td>
					<td>''' + current.correu + '''</td>
					<td>''' + str ( current.data ) + '''</td>
					''' )
			self.response.write ( '''</tr>''' )
		self.response.write ( '''</table>''' )

class UsersEuskaraHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		usuaris = Usuari.query ()
		self.response.write ( '<h1>Erabiltzaile erregistratuak</h1>' )
		self.response.write ( '<link rel="stylesheet" href="/styles/main.css">' )
		self.response.write ( '<link rel="stylesheet" href="/styles/table.css">' )
		self.response.write ( '''
			<table>
				<tr>
					<th>Izena</th>
					<th>Email</th>
					<th>Registrat</th>
				</tr>
		''' )
		for current in usuaris.fetch () :
			self.response.write ( ''' 
				<tr>
					<td>''' + current.nom + '''</td>
					<td>''' + current.correu + '''</td>
					<td>''' + str ( current.data ) + '''</td>
					''' )
			self.response.write ( '''</tr>''' )
		self.response.write ( '''</table>''' )

#**********************************************************************************

class MapMainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'mapa_ca.html', {} ) )

	def post ( self ) :
		mapurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
		address = self.request.get ( 'address' )
		url = mapurl + urllib.urlencode ( { 'address': address } )
		uh = urllib.urlopen ( url )
		data = uh.read ()
		js = json.loads ( str ( data ) )
		matrix = js [ 'results' ]
		if len ( matrix ) > 0 :
			adresa = matrix [0]['formatted_address']
			self.response.write ( '''Latitud: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>''' )
			self.response.write ( '''Longitud: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</br>''' )
			self.response.write ( '''@@@@@
				var latlong = { lat: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + ''', lng: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''};
				var mapa = new google.maps.Map( document.getElementById ( 'map' ), {
					zoom: 14,
					center: latlong
				});
				var marker = new google.maps.Marker ({
					position: latlong,
					map: map,
					title: ' ''' + adresa + ''' '
				});
				var content = '<div id="content">' + '<div id="site">' + '</div>' + '<h1 id="firstHeading" class="dirstHeading">''' + adresa + '''</h1>' +
				'<div id="bodyContent">' + '<p>Latitud: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>' +
				'Longitud: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</p>' + '</div>' + '</div>';
				var infowindow = new google.maps.InfoWindow({
					content: content
				});
				marker.addListener ( 'click', function () {
					infowindow.open ( mapa, marker );
				});			
			''' )
		else :
			self.response.write ( '''<br/> No s'ha trobat cap resultat''' )

class MapEnglishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'mapa_en.html', {} ) )

	def post ( self ) :
		mapurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
		address = self.request.get ( 'address' )
		url = mapurl + urllib.urlencode ( { 'address': address } )
		uh = urllib.urlopen ( url )
		data = uh.read ()
		js = json.loads ( str ( data ) )
		matrix = js [ 'results' ]
		if len ( matrix ) > 0 :
			adresa = matrix [0]['formatted_address']
			self.response.write ( '''Latitude: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>''' )
			self.response.write ( '''Longitude: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</br>''' )
			self.response.write ( '''@@@@@
				var latlong = { lat: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + ''', lng: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''};
				var mapa = new google.maps.Map( document.getElementById ( 'map' ), {
					zoom: 14,
					center: latlong
				});
				var marker = new google.maps.Marker ({
					position: latlong,
					map: map,
					title: ' ''' + adresa + ''' '
				});
				var content = '<div id="content">' + '<div id="site">' + '</div>' + '<h1 id="firstHeading" class="dirstHeading">''' + adresa + '''</h1>' +
				'<div id="bodyContent">' + '<p>Latitud: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>' +
				'Longitud: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</p>' + '</div>' + '</div>';
				var infowindow = new google.maps.InfoWindow({
					content: content
				});
				marker.addListener ( 'click', function () {
					infowindow.open ( mapa, marker );
				});			
			''' )
		else :
			self.response.write ( '''<br/> There are no results''' )

class MapSpanishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'mapa_es.html', {} ) )

	def post ( self ) :
		mapurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
		address = self.request.get ( 'address' )
		url = mapurl + urllib.urlencode ( { 'address': address } )
		uh = urllib.urlopen ( url )
		data = uh.read ()
		js = json.loads ( str ( data ) )
		matrix = js [ 'results' ]
		if len ( matrix ) > 0 :
			adresa = matrix [0]['formatted_address']
			self.response.write ( '''Latitud: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>''' )
			self.response.write ( '''Longitud: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</br>''' )
			self.response.write ( '''@@@@@
				var latlong = { lat: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + ''', lng: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''};
				var mapa = new google.maps.Map( document.getElementById ( 'map' ), {
					zoom: 14,
					center: latlong
				});
				var marker = new google.maps.Marker ({
					position: latlong,
					map: map,
					title: ' ''' + adresa + ''' '
				});
				var content = '<div id="content">' + '<div id="site">' + '</div>' + '<h1 id="firstHeading" class="dirstHeading">''' + adresa + '''</h1>' +
				'<div id="bodyContent">' + '<p>Latitud: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>' +
				'Longitud: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</p>' + '</div>' + '</div>';
				var infowindow = new google.maps.InfoWindow({
					content: content
				});
				marker.addListener ( 'click', function () {
					infowindow.open ( mapa, marker );
				});			
			''' )
		else :
			self.response.write ( '''<br/> No se han encontrado resultados''' )

class MapEuskaraHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'mapa_eu.html', {} ) )

	def post ( self ) :
		mapurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
		address = self.request.get ( 'address' )
		url = mapurl + urllib.urlencode ( { 'address': address } )
		uh = urllib.urlopen ( url )
		data = uh.read ()
		js = json.loads ( str ( data ) )
		matrix = js [ 'results' ]
		if len ( matrix ) > 0 :
			adresa = matrix [0]['formatted_address']
			self.response.write ( '''Latitudea: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>''' )
			self.response.write ( '''Longitudea: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</br>''' )
			self.response.write ( '''@@@@@
				var latlong = { lat: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + ''', lng: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''};
				var mapa = new google.maps.Map( document.getElementById ( 'map' ), {
					zoom: 14,
					center: latlong
				});
				var marker = new google.maps.Marker ({
					position: latlong,
					map: map,
					title: ' ''' + adresa + ''' '
				});
				var content = '<div id="content">' + '<div id="site">' + '</div>' + '<h1 id="firstHeading" class="dirstHeading">''' + adresa + '''</h1>' +
				'<div id="bodyContent">' + '<p>Latitud: ''' + str ( matrix[0]['geometry']['location']['lat'] ) + '''</br>' +
				'Longitud: ''' + str ( matrix[0]['geometry']['location']['lng'] ) + '''</p>' + '</div>' + '</div>';
				var infowindow = new google.maps.InfoWindow({
					content: content
				});
				marker.addListener ( 'click', function () {
					infowindow.open ( mapa, marker );
				});			
			''' )
		else :
			self.response.write ( '''<br/> Ez da inongo emaitzik aurkitu''' )
		

#**********************************************************************************

class PLoginMainHandler ( session_module.BaseSessionHandler ) :
	def get ( self ) :

		if self.session.get ( 'successfulLogin' ) :
			self.redirect ( '/pujar' )
			self.response.write ( '''
				<link rel="stylesheet" href="/styles/main.css">
				<a href="/plogout" class="button" style="float: right;">Sortir</a>
			''' )
		else :
			self.response.out.write ( template.render ( 'plogin_ca.html', {} ) )
	def post ( self ) :
		correu = self.request.get( "email" )
		contrasenya = self.request.get ( "password" )
		usuaris = Usuari.query ( ndb.AND ( Usuari.correu == correu, Usuari.contrasenya == contrasenya ) )
		if usuaris.count () > 0 :
			for eachUser in usuaris :
				self.session[ 'successfulLogin' ] = eachUser.nom
				self.session[ 'successfulEmail' ] = eachUser.correu
			self.response.write ( '''<script>parent.location.href=parent.location.href</script>''' )
		else :
			self.response.write ( '''<h6>Correu o contrasenya incorrectes</h6>''' )
			self.response.out.write ( template.render ( 'plogin_ca.html', {} ) )


class PLogoutMainHandler ( session_module.BaseSessionHandler ) :
	def get ( self ) :
		del self.session['successfulLogin']
		del self.session['successfulEmail']
		self.response.out.write ( template.render ( 'plogin_ca.html', {} ) )

FORM_SUBIR_FOTO = """
	<html><head><link rel="stylesheet" href="/styles/main.css"></head><body>
	<div style="float: right;">
	<form method="get" action="/es"><input type="submit" value="Volver"></form>
	</div>
	<form action="%(url)s" method="POST" enctype="multipart/form-data">
	<input type="file" name="file"><br>
	<input type="radio" name="access" value="public" checked="checked"/>
	Public
	<input type="radio" name="access" value="private" /> Private <p>
	<input type="submit" name="submit" value="Subir">
	</form><br>
	<form method="get" action="/galeria"><input type="submit" value="Galeria"></form>
	</body></html>"""

class UploadMainHandler ( session_module.BaseSessionHandler, blobstore_handlers.BlobstoreUploadHandler ) :
	def get ( self ) :
		if self.session.get ( 'successfulLogin' ) :
			upload_url = blobstore.create_upload_url ( '/pujar' )
			self.response.out.write ( FORM_SUBIR_FOTO % { 'url' : upload_url } )
	def post ( self ) :
		foto = self.get_uploads ( 'file' )
		blob_info = foto[0]
		img = Image ( user = self.session.get ( 'successfulEmail' ), public = self.request.get ( "access" ) == "public", blob_key = blob_info.key () )
		img.put ()
		self.redirect ( '/galeria' )

class GalleryMainHandler ( session_module.BaseSessionHandler, blobstore_handlers.BlobstoreDownloadHandler ) :
	def get ( self ) :
		if not self.session.get ( 'successfulLogin' ) :
			self.redirect ( '/plogin' )
		else :
			fotoPublica = Image.query ().filter ( Image.public == True )
			fotoPrivada = Image.query ().filter ( Image.public == False ).filter ( Image.user == self.session.get ( 'successfulLogin' ) )
			sourceHTML = '''
				<div style="position: absolute; height: 5000px; width: 5000px;">
					<form method="get" action="/es">
						<input type="submit" value="Volver">
					</form>
					<head>
						<link rel="stylesheet" href="/styles/main.css">
					</head>
					<body>
						<h1>Galeria</h1>
						'''
			for i, picture in enumerate ( fotoPublica ) :
				sourceHTML += '''<img name="img{0}" src="/serve/{1}" height="200" width="200" onmouseover="this.src='/images/publica.png'" onmouseout="this.src='/serve/{1}'"/>'''.format ( i, picture.blob_key )
			for i, picture in enumerate ( fotoPrivada ) :
				sourceHTML += '''<img name="img{0}" src="/serve/{1}" height="200" width="200" onmouseover="this.src='/images/publica.png'" onmouseout="this.src='/serve/{1}'"/>'''.format ( i, picture.blob_key )
			sourceHTML += '</body></div>'
			self.response.out.write ( sourceHTML )

class ServeHandler ( blobstore_handlers.BlobstoreDownloadHandler ) :
	def get ( self, resource ) :
		resource = str ( urllib.unquote ( resource ) )
		blob_info = blobstore.BlobInfo.get ( resource )
		self.send_blob ( blob_info )

#**********************************************************************************

app = webapp2.WSGIApplication ( [
	( '/', MainHandler ),
	( '/en', EnglishHandler ),
	( '/es', SpanishHandler ),
	( '/eu', EuskaraHandler ),
	( '/registre', RegisterMainHandler ),
	( '/en/registre', RegisterEnglishHandler ),
	( '/es/registre', RegisterSpanishHandler ),
	( '/eu/registre', RegisterEuskaraHandler ),
	( '/usuaris', UsersMainHandler ),
	( '/en/usuaris', UsersEnglishHandler ),
	( '/es/usuaris', UsersSpanishHandler ),
	( '/eu/usuaris', UsersEuskaraHandler ),
	( '/validar/', ValidateMainHandler ),
	( '/mapa', MapMainHandler ),
	( '/en/mapa', MapEnglishHandler ),
	( '/es/mapa', MapSpanishHandler ),
	( '/eu/mapa', MapEuskaraHandler ),
	( '/plogin', PLoginMainHandler ),
	( '/plogout', PLogoutMainHandler ),
	( '/pujar', UploadMainHandler ),
	( '/galeria', GalleryMainHandler ),
	( '/serve/([^/]+)?', ServeHandler ),
], config=myconfig_dict, debug = True)