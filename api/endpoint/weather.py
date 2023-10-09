from fastapi import APIRouter, Depends, HTTPException
from typing import List

router = APIRouter()


@router.get("/weather/")
def get_users(skip: int = 0, limit: int = 10):
    return "100°"
