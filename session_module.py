import webapp2
from webapp2_extras import sessions

#myconfig_dict = {}
#myconfig_dict[ 'webapp2_extras.sessions' ] = {
#	'secret_key' : 'my-super-secret-key-somemorearbitarythingstosay',
#}

class BaseSessionHandler ( webapp2.RequestHandler ) :
	def dispatch ( self ) :
		self.session_store = sessions.get_store ( request = self.request )
		try:
			webapp2.RequestHandler.dispatch ( self )
		finally:
			self.session_store.save_sessions ( self.response )

	@webapp2.cached_property
	def session ( self ) :
		return self.session_store.get_session()