from fastapi import APIRouter, Depends, HTTPException
from services.auth.auth_service import AuthService
from models.auth_models import UserLogin, UserRegister

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
async def login(user_data: UserLogin):
    try:
        token = await AuthService.authenticate_user(user_data.username, user_data.password)
        return {"token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/register")
async def register(user_data: UserRegister):
    try:
        await AuthService.create_user(user_data)
        return {"message": "User created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))