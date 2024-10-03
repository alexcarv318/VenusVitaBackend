from datetime import datetime, timedelta
from fastapi import APIRouter
from starlette.exceptions import HTTPException
from pydantic import BaseModel, EmailStr
from starlette.status import HTTP_429_TOO_MANY_REQUESTS

from .. import config
from ..utils import send_email as smtp_client
from ..utils.redis_cli import redis_client


router = APIRouter()


class AppointmentRequest(BaseModel):
    name: str
    surname: str
    phone: str
    email: EmailStr


@router.post("/create")
async def make_appointment(request: AppointmentRequest):
    if not is_request_allowed(request.email):
        return HTTPException(
            status_code=HTTP_429_TOO_MANY_REQUESTS,
            detail="You can only make one appointment per day."
        )

    send_mail(request.name, request.surname, request.phone, request.email)

    save_request_time(request.email)

    return {"success": "Your appointment request has been submitted!"}


def send_mail(name: str, surname: str, phone: str, email: str):
    message = (
        f'''<h2>До вас хоче записатися клієнт:</h2>
            <p>Ім'я: {name + " " + surname}</p>
            <p>Телефон: {phone}</p>
            <p>Email: {email}</p>
            <h3>Зв'яжіться з ним, будь ласка!</h3>.'''
    )

    smtp_client.send_email(
        sender=email,
        receiver=config.SMTP_USERNAME,
        subject='Запис на візит!',
        message=message
    )


def is_request_allowed(email: str) -> bool:
    last_request_time = redis_client.get(email)
    if last_request_time:
        last_request_time = datetime.strptime(last_request_time.decode('utf-8'), '%Y-%m-%d %H:%M:%S')
        if datetime.now() - last_request_time < timedelta(days=1):
            return False
    return True


def save_request_time(email: str):
    redis_client.set(email, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

