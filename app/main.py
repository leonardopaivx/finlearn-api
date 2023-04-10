from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import setting
from app.api.v1.api import api_router as router_v1

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
