from datetime import date
from sqlalchemy.orm import Session
from . import models, schemas

def get_rate_by_date(db: Session, rate_date: date):
    return db.query(models.CurrencyRate).filter(models.CurrencyRate.date == rate_date).first()

def create_rate(db: Session, rate: schemas.CurrencyRateCreate):
    db_rate = models.CurrencyRate(date=rate.date, rate=rate.rate)
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate

def get_average_rate(db: Session, start_date: date, end_date: date):
    rates = db.query(models.CurrencyRate).filter(models.CurrencyRate.date >= start_date).filter(models.CurrencyRate.date <= end_date).all()
    if not rates:
        return None
    return sum(rate.rate for rate in rates) / len(rates)
