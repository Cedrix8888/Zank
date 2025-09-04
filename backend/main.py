from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.api.img_routes import router as img_router
from config import FRONT_URL
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONT_URL],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(img_router, prefix="/api/img")


