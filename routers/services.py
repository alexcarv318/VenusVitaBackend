from fastapi import APIRouter, Depends
from api.dependencies import get_service_topics_repository, get_services_repository

router = APIRouter()

@router.get("/topics")
def get_all_service_topics(
    service_topics_repository=Depends(get_service_topics_repository)
):
    return service_topics_repository.get_all()


@router.get("/topics-with-images")
def get_all_service_topics_with_images(
    service_topics_repository=Depends(get_service_topics_repository)
):
    return service_topics_repository.get_all_with_images()


@router.get("/services")
def get_all_services(
    services_repository=Depends(get_services_repository)
):
    return services_repository.get_all()


@router.get("/services/{topic_id}")
def get_services_by_topic_id(
    topic_id: str,
    services_repository=Depends(get_services_repository)
):
    print("f")
    return services_repository.get_by_topic_id(topic_id)