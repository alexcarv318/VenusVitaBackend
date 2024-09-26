def get_db():
    from api.repositories.db import db
    return db

def get_service_topics_repository():
    from api.repositories.service_topics import ServiceTopicsRepository
    return ServiceTopicsRepository(database=get_db())

def get_services_repository():
    from api.repositories.services import ServicesRepository
    return ServicesRepository(database=get_db())