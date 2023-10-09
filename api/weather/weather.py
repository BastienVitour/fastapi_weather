from fastapi import APIRouter, Depends, HTTPException
from typing import List
import json

router = APIRouter()


@router.get("/weather/")
def get_weather(skip: int = 0, limit: int = 10):
    return "100°"


@router.get("/weather/temp/tmin/")
def get_min_temperature():
    """
    Function to get the data for the day when the temperature was the lowest
    """
    try:
        json_data = json.load(open("rdu-weather-history.json", "r", encoding="utf-8"))
        lowest_temp = json_data[0]["tmin"]
        lowest_temp_data = json_data[0]
        for daily_weather in json_data:
            if daily_weather["tmin"] < lowest_temp:
                lowest_temp = daily_weather["tmin"]
                lowest_temp_data = daily_weather
        return {"data": lowest_temp_data}
    except HTTPException:
        return {"Error": "Error"}


@router.get("/weather/temp/tmax")
def get_max_temperature():
    """
    Function to get the data for the day when the temperature was the highest
    """
    try:
        json_data = json.load(open("rdu-weather-history.json", "r", encoding="utf-8"))
        highest_temp = json_data[0]["tmax"]
        highest_temp_data = json_data[0]
        for daily_weather in json_data:
            if daily_weather["tmax"] > highest_temp:
                highest_temp = daily_weather["tmax"]
                highest_temp_data = daily_weather
        return {"data": highest_temp_data}
    except HTTPException:
        return {"Error": "Error"}
