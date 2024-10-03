import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import appointments, services

app = FastAPI()

app.include_router(router=appointments.router, prefix="/appointment", tags=["appointment"])
app.include_router(router=services.router, prefix="/services", tags=["services"])

origins = [
    "https://venusvita.com.ua",
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
