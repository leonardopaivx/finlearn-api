from enum import StrEnum
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.middleware.auth import authenticate_user_api_endpoints
from app.core.middleware.db import get_db
from app.core.middleware.error_handler import ErrorModel

from app.core.models import IdOut
from app.domain.social_media.models.talk_model import (
    TalkInputSchema,
    TalkOutputSchema,
    TalkSchema,
)
from app.domain.social_media.repositories import talk_repository
from app.domain.user.entities.user import User


router = APIRouter()

class InvestmentTypes(StrEnum):
    CDB = "CDB"
    SAVINGS = "SAVINGS"
    TRUST_FUND = "TRUST_FUND"

class PracticeInputSchema(BaseModel):
    rate : InvestmentTypes
    initial_investment: float
    duration: int
    monthly_investment: float | None

@router.post('/')
def calculate_investment_return(input:PracticeInputSchema):
    rate_value = 6 if input.rate == "CDB" else (8 if input.rate == "TRUST_FUND" else 4.5)
    investment = input.initial_investment
    monthly_rate = rate_value / 12 / 100  # Converting the annual rate to monthly rate
    months = input.duration * 12
    
    for _ in range(months):
        investment += input.monthly_investment
        investment *= (1 + monthly_rate)
    
    return investment
