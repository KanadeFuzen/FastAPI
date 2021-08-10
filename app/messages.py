"""Friendly messsages"""

from fastapi import APIRouter

router = APIRouter()


@router.get('/hello')
async def hello():
    """You look like a whole clown right now. 🤡"""
    pass