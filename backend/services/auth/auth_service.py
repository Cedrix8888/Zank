from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext
from models.db_models import User
from utils.database import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key"  # Move to environment variables

class AuthService:
    @staticmethod
    async def authenticate_user(username: str, password: str):
        db = next(get_db())
        user = db.query(User).filter(User.username == username).first()
        
        if not user or not pwd_context.verify(password, user.password):
            raise ValueError("Invalid username or password")
            
        access_token = jwt.encode(
            {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=1)},
            SECRET_KEY,
            algorithm="HS256"
        )
        
        return access_token

    @staticmethod
    async def create_user(user_data):
        db = next(get_db())
        
        if db.query(User).filter(User.username == user_data.username).first():
            raise ValueError("Username already exists")
            
        hashed_password = pwd_context.hash(user_data.password)
        db_user = User(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user