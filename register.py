#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.ext.webapp \
	import template

class MainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_ca.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_ca.html', {} ) )
		self.response.write ( '<h2>Formulari rebut</h2>' )
		self.response.write ( "Nom: %s <br>" % self.request.get ( 'username' ) )

class EnglishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_en.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_en.html', {} ) )
		self.response.write ( '<h2>Form received</h2>' )
		self.response.write ( "Name: %s <br>" % self.request.get ( 'username' ) )

class SpanishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_es.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_es.html', {} ) )
		self.response.write ( '<h2>Formulario recibido</h2>' )
		self.response.write ( "Nombre: %s <br>" % self.request.get ( 'username' ) )

class EuskaraHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.out.write ( template.render ( 'register_eu.html', {} ) )

	def post ( self ) :
		self.response.out.write ( template.render ( 'register_eu.html', {} ) )
		self.response.write ( '<h2>Formularioa ondo jaso da</h2>' )
		self.response.write ( "Izena: %s <br>" % self.request.get ( 'username' ) )

app = webapp2.WSGIApplication ( [
	( '/registre', MainHandler ),
	( '/en/registre', EnglishHandler ),
	( '/es/registre', SpanishHandler ),
	( '/eu/registre', EuskaraHandler )
], debug = True)