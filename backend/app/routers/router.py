from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def hello(name: str):
    return {"message": f"Hello {name}"}

"""
routes:

POST /config
GET /config

GET /accounts
POST /accounts

GET /proxy
POST /proxy

POST /action

GET /logs

GET /status
"""