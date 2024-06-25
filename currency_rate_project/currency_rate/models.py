from sqlalchemy import Column, Integer, String, Float, Date 
from .database import Base

class CurrencyRate(Base):
    __tablename__ = "currency_rates"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, index=True)
    rate = Column(Float, nullable=False)
