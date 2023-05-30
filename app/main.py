from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import setting
from app.api.v1.api import api_router as router_v1
from app.core.middleware.db import get_db

if not setting.TEST_ENV:
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_v1, prefix="/v1")

@app.get("/")
def healthcheck(db: Session = Depends(get_db)):
    db.execute(select(1))
    return {"status": True}
