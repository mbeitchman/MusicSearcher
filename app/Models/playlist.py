class Playlist:
	"""
	This class is the model for a playlist.
	The model has a list of Song models and a name.
	"""
	def __init__(self, name):
		self.songs = []
		self.name = name
