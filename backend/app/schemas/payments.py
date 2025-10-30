from pydantic import BaseModel, Field

class Payments(BaseModel):
    amount: float = Field(..., max_length=12)
    status: str = Field(..., default='completed')