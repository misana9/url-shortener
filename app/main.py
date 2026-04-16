from fastapi import FastAPI
from .routers import url_shortener,url_finder,users,auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .config import settings


app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://url-shortener-production-3c68.up.railway.app",
    "https://gentle-education-production-3cdd.up.railway.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users.router)
app.include_router(url_shortener.router)
app.include_router(url_finder.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message" : "hello World"}
