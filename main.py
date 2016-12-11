#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

class EnglishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.write ( '<html><body><head><link rel="stylesheet" href="/styles/main.css"</head>' )
		self.response.write ( '<h1>Hello world!</h1><img src="/images/uk.gif"/>' )
		self.response.write ( '</body></html>' )

class SpanishHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.write ( '<html><body><head><link rel="stylesheet" href="/styles/main.css"</head>' )
		self.response.write ( '<h1>¡Hola mundo!</h1><img src="/images/espanya.gif"/>' )
		self.response.write ( '</body></html>' )

class EuskaraHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.write ( '<html><body><head><link rel="stylesheet" href="/styles/main.css"</head>' )
		self.response.write ( '<h1>Kaixo mundua!</h1><img src="/images/ikurrinya.gif"/>' )
		self.response.write ( '</body></html>' )

class MainHandler ( webapp2.RequestHandler ) :
	def get ( self ) :
		self.response.write ( '<html><body><head><link rel="stylesheet" href="/styles/main.css"</head>' )
		self.response.write ( '<h1>Hola mon!</h1><img src="/images/senyera.gif"/>' )
		self.response.write ( '</body></html>' )

app = webapp2.WSGIApplication ( [
	( '/', MainHandler ),
	( '/en', EnglishHandler ),
	( '/es', SpanishHandler ),
	( '/eu', EuskaraHandler )
], debug = True)