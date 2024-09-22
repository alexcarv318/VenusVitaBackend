from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import appointments

app = FastAPI()

app.include_router(router=appointments.router, prefix="/appointment", tags=["appointment"])

origins = [
    "https://venusvita.com.ua",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

