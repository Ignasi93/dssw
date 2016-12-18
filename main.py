#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import urllib
import re
from google.appengine.ext.webapp \
	import template
from google.appengine.api import images
from google.appengine.ext import ndb

class Usuari ( ndb.Model ) :
	nom = ndb.StringProperty ( required = True )
	contrasenya = ndb.StringProperty ( required = True )
	correu = ndb.StringProperty ( required = True )
	data = ndb.DateTimeProperty ( auto_now_add = True )

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

class UsersMainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		usuaris = Usuari.query ()
		self.response.write ( '<h1>Usuaris registrats</h1>' )
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
], debug = True)