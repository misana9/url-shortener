from fastapi import FastAPI
from .routers import url_shortener,url_finder,users,auth
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/")
async def root():
    return {"message" : "hello World"}