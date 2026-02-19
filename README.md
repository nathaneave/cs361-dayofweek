# CS361 (Group 17) - Small Pool Microservice: Day of Week

**What does this microservice do?**

This microservice allows the user to provide a date, and returns the day of the week that date is on. In addition, if the provided date is a US federal holiday, the microservice will provide the name of the holiday.

**How do I request data from this microservice?**

To request data from this microservice, you will need to make an `HTTP GET request` to the `/dayofweek` endpoint. You must pass the `event_date` as a string in the form of `YYYY-MM-DD` as a query parameter.

_Example call:_ `GET http://127.0.0.1:8000/dayofweek?event_date=2026-01-02`

**How will I receive data from this microservice?**

The microservice will return a `JSON object`. The object will have two name/value pairs. The name/value pairs will be `day_of_week` which is a string that is the day of the week that the provided date is on and `holiday` which is a string that indicates, if the date is a holiday, what holiday the date is on. If the date is not a holiday, then `holiday` will be null.

_Example response (valid date, not a holiday)_:

Status code: `200`
```yaml
{
"day_of_week": "Wednesday",
"holiday": null
}
```

_Example response (valid date, holiday)_:

Status code: `200`
```yaml
{
"day_of_week": "Monday",
"holiday": "Washington's Birthday"
}
```

_Example response (invalid date)_:

Status code: `400`
```yaml
{
"detail": "Invalid date format. Please use YYYY-MM-DD."
}
```
**UML Sequence Diagram**

<img width="525" height="395" alt="image" src="https://github.com/user-attachments/assets/3f5ec432-3793-4f6d-8e92-3eaceab8915f" />
