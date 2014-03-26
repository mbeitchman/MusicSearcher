from app.DataLayer import datastore
from app.Models import playlist
from app.Models import song

class PlaylistDataLayer:
	"""
	This class manages the datastores for the playlist service.
	The purpose of this layer is to manage connections to the datastores,
	map members to commands, handle error cases such as timeouts and deadlocks.
	In a production system, this component could use a document storage system
	such as mongodb for the datastore.
	"""
	def __init__(self, datastore):
		self.datastore = datastore

	def create(self, name):
		""" Creates a new playlist. """
		return self.datastore.try_add(name, playlist.Playlist(name))

	def get(self, name):
		""" Returns the playlist."""
		return self.datastore.try_get(name)

	def get_all(self):
		""" Returns all of the playlists in the datastore."""
		return self.datastore.try_get_all()

	def delete(self, name):
		""" Deletes a playlist """
		return self.datastore.try_delete(name)

	def set_song(self, name, song):
		""" Adds a song to the playlist. """
		playlist = self.get(name)
		playlist.songs.append(song)

		return self.datastore.try_update(name, playlist)

	def remove_song(self, name, song):
		""" Removes the first match of a song from the playlist. """
		playlist = self.get(name)
		for i, s in enumerate(playlist.songs):
			isequal = s.name == song.name and s.url == song.url and \
				s.album == song.album and s.artist == song.artist
			if isequal:
				del playlist.songs[i]
				break

		return self.datastore.try_update(name, playlist)