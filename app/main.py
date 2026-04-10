from fastapi import FastAPI
from .routers import url_shortener,url_finder,users,auth


app = FastAPI()

app.include_router(users.router)
app.include_router(url_shortener.router)
app.include_router(url_finder.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message" : "hello World"}