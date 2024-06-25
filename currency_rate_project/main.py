from fastapi import FastAPI, Depends, HTTPException
import requests
from sqlalchemy.orm import Session
from datetime import date, datetime
from . import crud, models, schemas, dependencies, utils
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/rate", response_model=schemas.CurrencyRate)
def read_rate(date: str = None, start_date: str = None, end_date: str = None, db: Session = Depends(dependencies.get_db)):
    if date:
        try:
            target_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
        
        db_rate = crud.get_rate_by_date(db, target_date)
        if db_rate:
            return db_rate
        
        try:
            rate_value = utils.fetch_rate_for_date(target_date)
            rate = schemas.CurrencyRateCreate(date=target_date, rate=rate_value)
            return crud.create_rate(db, rate)
        except requests.RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    elif start_date and end_date:
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
        
        avg_rate = crud.get_average_rate(db, start_date_obj, end_date_obj)
        if avg_rate is None:
            raise HTTPException(status_code=404, detail="No data available for the specified date range")
        
        return {"start_date": start_date, "end_date": end_date, "average_rate": avg_rate}
    
    else:
        today = date.today()
        db_rate = crud.get_rate_by_date(db, today)
        if db_rate:
            return db_rate
        
        try:
            rate_value = utils.fetch_rate_for_date(today)
            rate = schemas.CurrencyRateCreate(date=today, rate=rate_value)
            return crud.create_rate(db, rate)
        except requests.RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))
