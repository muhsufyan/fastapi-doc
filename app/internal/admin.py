# handling "admin", APIRouter (sub bagiaan dari API, nantinya dikumpulkan dlm global api di main)
from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
