# Flight Management System

## Overview

This project consists of two Python scripts: `process_flights.py` and `api.py`. The purpose of this system is to manage flight data stored in a CSV file,
allowing for the addition of new flight entries and the processing of existing flight data to determine their success status.

## Files

1. **process_flights.py**: This script reads a CSV file containing flight information, processes the data to calculate the success or failure of flights based on arrival and departure times, and overwrites the same file with the updated information.

2. **api.py**: This script sets up a Flask web API that allows users to:
   - Add new flights to the CSV file.
   - Retrieve flight information by flight ID.

## Requirements

- Python
- Flask
- Pandas

- API Endpoints
Add a Flight
Endpoint: /flight
Method: POST
Request Body:
json
[
    {
        "flight ID": "B15",
        "Arrival": "15:00",
        "Departure": "18:30"
    },
    {
        "flight ID": "A25",
        "Arrival": "18:00",
        "Departure": "21:30"
    }
]
Response:
Success (200):
{
    "message": "Flights added successfully"
}
Error (400):
{
    "error": "Missing fields in flight data"
}

Get Flight Information
Endpoint: /flight/<flight_id>
Method: GET
Response:
Success (200): Returns flight details in JSON format.
Error (404):
{
    "error": "Flight not found"
}
