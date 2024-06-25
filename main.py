from urllib import request
from fastapi import FastAPI, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from datetime import date
from . import crud, models, schemas, dependencies, utils
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/rate", response_model=schemas.CurrencyRate)
def read_rate(date: str = None, start_date: str = None, end_date: str = None, db: Session = Depends(dependencies.get_db)):
    if date:
        db_rate = crud.get_rate_by_date(db, date)
        if db_rate:
            return db_rate
        try:
            rate_value = utils.fetch_rate_for_date(date)
            rate = schemas.CurrencyRateCreate(date=date, rate=rate_value)
            return crud.create_rate(db, rate)
        except request.HTTPError as e:
            raise HTTPException(status_code=400, detail=str(e))
    elif start_date and end_date:
        avg_rate = crud.get_average_rate(db, start_date, end_date)
        if avg_rate is None:
            raise HTTPException(status_code=404, detail="No data available for the specified date range")
        return {"start_date": start_date, "end_date": end_date, "average_rate": avg_rate}
    else:
        today = date.today().isoformat()
        db_rate = crud.get_rate_by_date(db, today)
        if db_rate:
            return db_rate
        try:
            rate_value = utils.fetch_rate_for_date(today)
            rate = schemas.CurrencyRateCreate(date=today, rate=rate_value)
            return crud.create_rate(db, rate)
        except request.HTTPError as e:
            raise HTTPException(status_code=400, detail=str(e))
