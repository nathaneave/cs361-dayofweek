from fastapi import FastAPI, HTTPException
from datetime import date
import holidays

app = FastAPI()

@app.get("/dayofweek")
def root(event_date: str):
    #event_date should be in the format YYYY-MM-DD
    #try to convert the provided values a date object, if not return 400 error code
    try:
        target_date = date.fromisoformat(event_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Please use YYYY-MM-DD.")
    
    #creates a dict-like object with the holidays in the United States
    holiday_cal = holidays.US()
    #check if our target_date is a holiday
    if target_date in holiday_cal:
        #if it is, update the holiday name accordingly
        holiday_name = holiday_cal.get(target_date)
    else:
        holiday_name = None

    #.weekday() returns 0 for Monday and 6 for Sunday, so our list starts with Monday
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week_index = target_date.weekday()

    return {"day_of_week": days_of_week[day_of_week_index], "holiday": holiday_name}
