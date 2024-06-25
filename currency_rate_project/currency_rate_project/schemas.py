from pydantic import BaseModel 
from datetime import date

class CurrencyRateBase(BaseModel):
    date: date
    rate: float

class CurrencyRateCreate(CurrencyRateBase):
    pass

class CurrencyRate(CurrencyRateBase):
    id: int

    class Config:
        orm_mode = True
