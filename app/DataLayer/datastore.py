class DataStore:
	""" 
	This class implements a very very simple in memory key-value store.
	In an actual production system, I would use a more sophisticated 
	datastorage system. A document store such as mongo would be apporpriate
	for handling playlists and a caching system such as Redis would be
	appropriate for the search cache.
	"""	
	def __init__(self):
		self.db = dict()

	def try_get(self, key):
		""" Tries to get a value from the datastore. """
		if key not in self.db:
			return None

		return self.db[key]

	def try_get_all(self):
		""" Gets all of the values from the datastore. """
		return self.db.values()

	def try_add(self, key, value):
		""" Tries tp add a value to the datastore. """
		if key in self.db:
			raise KeyError("DataStore:TryAdd - Key already exists in the dictionary.")

		self.db[key] = value

		return value

	def try_update(self, key, value):
		""" Tries to update a value in the datastore. """
		if key not in self.db:
			raise KeyError("DataStore:TryUpdate - Key does not exist in the dictionary.")

		self.db[key] = value

		return value

	def try_remove(self, key):
		""" Tries to remove a value from the datastore. """
		if key in self.db:
			del self.db[key]

		return key

