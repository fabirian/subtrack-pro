from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str = Field(..., min_length=5, max_length=60)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=12)
    

    