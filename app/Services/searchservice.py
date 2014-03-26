from app.DataLayer import searchdatalayer

class SearchService:
	"""
	This class is the external entry point for the search service.
	The service is used by the music searcher app for findig tracks.
	"""
	def __init__(self, datastore):
		# The constructor takes in the datastore as a param so that a mock datastore
		# can be injected into the datalayer for testability.
		self.search_datalayer = searchdatalayer.SearchDataLayer(datastore)

	def search(self, search_request):
		""" 
		Runs a search for the given search request parameter
		"""
		try:
			response = self.search_datalayer.search(search_request)
		except Exception, e:
			# log exception
			response = None
		
		return response