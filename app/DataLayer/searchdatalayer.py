import json
import urllib2
from app.DataLayer import datastore
from app.Models import song

class SearchDataLayer:
	"""
	This class manages the datastores for the search service.
	The purpose of this layer is to manage connections to the datalayer,
	map members to commands, handle error cases such as timeouts and deadlocks.
	In a production system, a system like redis would be a good choice for the
	caching layer.
	"""
	def __init__(self, datastore):
		self.datastore = datastore

	def search(self, search_request):
		""" 
		This is the public function for the search.
		The function first checks for the search results in the cache.
		If the results are not in the cache, the function gets the results
		from the Spotify web service and stores the results in cache.
		"""
		results = self.get_search_results_from_cache(search_request)
		if not results:
			results = self.get_search_results_from_spotify(search_request)
			self.add_search_results_to_cache(search_request, results)
		
		return results

	# internal functions
	def get_search_results_from_cache(self, search_request):
		# checks the cache for the search results
		return self.datastore.try_get(search_request)

	def add_search_results_to_cache(self, search_request, result):
		# adds the results to the cache
		return self.datastore.try_add(search_request, result)

	def get_search_results_from_spotify(self, search_request):
		# get the search results from Spotify
		search_request = urllib2.quote(search_request.encode('utf-8'))
		response = urllib2.urlopen("http://ws.spotify.com/search/1/track.json?q="+search_request)
		
		search_result_objects = json.load(response)
		
		return self.parse_tracks_from_spotify(search_result_objects['tracks'])

	def parse_tracks_from_spotify(self, tracks):
		# parse the results from Spotify into the Song model
		result = list()
		for track in tracks:
			s = song.Song(name = track['name'], album = track['album']['name'], 
						artist = track['artists'][0]['name'], url = track['href'])

			result.append(s)

		return result

