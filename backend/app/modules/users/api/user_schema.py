# DTOs / Request & Response models
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr


# 🔹 Base compartido
class UserBase(BaseModel):
    email: EmailStr


# 🔹 Para crear usuario (request)
class UserCreate(UserBase):
    password: str


# 🔹 Para devolver usuario (response)
class UserResponse(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # necesario para SQLAlchemy (Pydantic v2)
