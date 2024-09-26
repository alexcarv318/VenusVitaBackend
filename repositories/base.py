class BaseRepository:

    _collection_name = None

    def __init__(self, database):
        self._db = database
        self._collection = database[self._collection_name]

    @property
    def collection(self):
        return self._db[self._collection_name]