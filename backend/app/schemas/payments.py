from pydantic import BaseModel, Field

class Payments(BaseModel):
    amount: float = Field(..., ge=0.01, le=10000)
    status: str = Field(default='completed')
