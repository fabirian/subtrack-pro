from pydantic import BaseModel, Field

class Category(BaseModel):
    title: str = Field(..., min_length=6, max_length=20)
    description: str | None = None