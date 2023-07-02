from fastapi import FastAPI
from routes import router as police_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.include_router(police_router, prefix="/police", tags=["police"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)




