from .currency_rate_project import models 
from sqlalchemy.orm import Session 
from .currency_rate_project import schemas 

def get_rate_by_date(db: Session, date: str):
    return db.query(models.CurrencyRate).filter(models.CurrencyRate.date == date).first()

def create_rate(db: Session, rate: schemas.CurrencyRateCreate):
    db_rate = models.CurrencyRate(date=rate.date, rate=rate.rate)
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate

def get_average_rate(db: Session, start_date: str, end_date: str):
    rates = db.query(models.CurrencyRate).filter(models.CurrencyRate.date >= start_date, models.CurrencyRate.date <= end_date).all()
    if not rates:
        return None
    avg_rate = sum(rate.rate for rate in rates) / len(rates)
    return avg_rate
