#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
from google.appengine.ext.webapp \
	import template

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

class RegisterMainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_ca.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_ca.html', {} ) )
		self.response.write ( '<h2>Formulari rebut</h2>' )
		self.response.write ( "Nom: %s <br>" % self.request.get ( 'username' ) )

class RegisterEnglishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_en.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_en.html', {} ) )
		self.response.write ( '<h2>Form received</h2>' )
		self.response.write ( "Name: %s <br>" % self.request.get ( 'username' ) )

class RegisterSpanishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_es.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_es.html', {} ) )
		self.response.write ( '<h2>Formulario recibido</h2>' )
		self.response.write ( "Nombre: %s <br>" % self.request.get ( 'username' ) )

class RegisterEuskaraHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_eu.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_eu.html', {} ) )
		self.response.write ( '<h2>Formularioa ondo jaso da</h2>' )
		self.response.write ( "Izena: %s <br>" % self.request.get ( 'username' ) )

app = webapp2.WSGIApplication ( [
	( '/', MainHandler ),
	( '/en', EnglishHandler ),
	( '/es', SpanishHandler ),
	( '/eu', EuskaraHandler ),
	( '/registre', RegisterMainHandler ),
	( '/en/registre', RegisterEnglishHandler ),
	( '/es/registre', RegisterSpanishHandler ),
	( '/eu/registre', RegisterEuskaraHandler )
], debug = True)