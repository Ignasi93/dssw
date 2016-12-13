#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
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

app = webapp2.WSGIApplication ( [
	( '/', MainHandler ),
	( '/en', EnglishHandler ),
	( '/es', SpanishHandler ),
	( '/eu', EuskaraHandler )
], debug = True)