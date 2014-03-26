class Song:
	"""
	This class is the model for a song.
	The song model has a name, artist, album and url.
	"""
	def __init__(self, name, artist, album, url):
		self.name = name
		self.artist = artist
		self.album = album
		self.url = url