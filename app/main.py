from fastapi import FastAPI
from .routers import url_shortener,url_finder,users,auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
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

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def index():
    return HTMLResponse(open("frontend/index.html").read())


@app.get("/")
async def root():
    return {"message" : "hello World"}