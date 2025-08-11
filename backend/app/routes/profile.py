from fastapi import APIRouter
from app.supabase_client import supabase

router = APIRouter()

@router.post("/create-profile")
def create_profile(email: str, username: str):
    data = supabase.table("profiles").insert({
        "email": email,
        "username": username
    }).execute()
    return {"status": "success", "data": data.data}
