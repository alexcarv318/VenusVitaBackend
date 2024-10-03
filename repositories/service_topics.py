from .base import BaseRepository
from ..utils.parse_json import parse_json


class ServiceTopicsRepository(BaseRepository):

    _collection_name = 'service_topics'

    def get_all(self):
        topics = self.collection.find()
        return parse_json(topics)

    def get_all_with_images(self):
        topics = self.get_all()
        topics = filter(lambda topic: topic.get('image_url') is not None, topics)
        return list(topics)