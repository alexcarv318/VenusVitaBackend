from repositories.base import BaseRepository
from utils.parse_json import parse_json


class ServicesRepository(BaseRepository):

    _collection_name = "services"

    def get_all(self):
        services = self._collection.find()
        return parse_json(services)

    def get_by_topic_id(self, topic_id):
        criterion = {"topic_id": topic_id}
        services = self._collection.find(criterion)
        return parse_json(services)