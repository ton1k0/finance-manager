from fastapi import FastAPI
from routers import user, finance, authentication
import models
from database import engine


app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(finance.router)