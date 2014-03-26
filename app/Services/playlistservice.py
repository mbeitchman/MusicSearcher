from app.DataLayer import playlistdatalayer

class PlaylistService:
	"""
	This class is the external entry point for the playlist service.
	The playlist service is used by the music searcher app for managing 
	playlists.
	"""
	def __init__(self, datastore):
		# The constructor takes in the datastore as a param so that a mock datastore
		# can be injected into the datalayer for testability.
		self.playlist_datalayer = playlistdatalayer.PlaylistDataLayer(datastore)

	def create_playlist(self, name):
		"""
		Creates a new playlist with the pla
		"""
		try:
			response = self.playlist_datalayer.create(name)
		except Exception, e:
			# log exception
			response = None

		return response

	def get(self, name):
		"""
		Returns a playlist if it exists.
		"""
		try:
			response = self.playlist_datalayer.get(name)
		except Exception, e:
			# log exception
			response = None

		return response

	def get_all(self):
		"""
		Returns all of the playlists.
		"""
		try:
			response = self.playlist_datalayer.get_all()
		except Exception, e:
			# log exception
			response = None

		return response

	def delete(self, name):
		"""
		Deletes a playlist.
		"""
		try:
			response = self.playlist_datalayer.delete(name)
		except Exception, e:
			# log exception
			response = None

		return response		

	def set_song(self, name, song):
		"""
		Adds a song to the playlist.
		"""
		try:
			response = self.playlist_datalayer.set_song(name, song)
		except Exception, e:
			# log exception
			response = None

		return response

	def remove_song(self, name, song):
		"""
		Removes a song from the playlist.
		"""
		try:
			response = self.playlist_datalayer.remove_song(name, song)
		except Exception, e:
			# log exception
			response = None

		return response