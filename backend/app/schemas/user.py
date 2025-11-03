from pydantic import BaseModel, Field, EmailStr, field_validator
import re


class User(BaseModel):
    username: str = Field(..., min_length=1, max_length=60)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=12)
    
    @field_validator('username')
    def username_valid(cls, v):
        if not v.replace('_', '').isalnum():
            raise ValueError('The username can only contain letters, numbers, and underscores')
        return v
    
    @field_validator('password')
    def valid_password(cls, v):
        if not (re.search(r"[A-Z]", v)
                and re.search(r"[a-z]", v)
                and re.search(r"\d", v)
                ):
            raise ValueError('Password must contain at least one uppercase letter, one lowercase letter, and one number')
        return v
    

    