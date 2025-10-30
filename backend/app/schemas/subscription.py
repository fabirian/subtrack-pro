from pydantic import BaseModel, Field

class Subscription(BaseModel):
    service_name: str = Field(..., min_length=8, max_length=20)
    plan_name:str | None = None
    price: float
    renewal_date: date 
    billing_cycle: str = Field(..., min_length=4, max_length=8, default='monthly')
    status: str = Field(..., default='activate')
    