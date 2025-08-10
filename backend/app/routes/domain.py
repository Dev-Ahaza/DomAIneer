from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class DomainRequest(BaseModel):
    input_type: str
    user_msg: str

@router.post("/register")
def register_domain(request: DomainRequest):
    # Simulate AI domain assistant
    if request.input_type not in ["chat", "voive"]:
        raise HTTPException(status_code=400, detail="Invalid input type")

    ai_response = f"Checking domain availability for '{request.user_msg}'"

    return {"status": "success", "ai_response": ai_response}