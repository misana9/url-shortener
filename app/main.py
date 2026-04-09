from fastapi import FastAPI
from .routers import url_shortener,url_finder


app = FastAPI()

app.include_router(url_shortener.router)
app.include_router(url_finder.router)

@app.get("/")
async def root():
    return {"message" : "hello World"}