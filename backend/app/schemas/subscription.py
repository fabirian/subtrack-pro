from pydantic import BaseModel, Field, field_validator
import re
from datetime import date

class Subscription(BaseModel):
    service_name: str = Field(..., min_length=1, max_length=20)
    plan_name:str | None = None
    price: float = Field(..., gt=0)
    renewal_date: date 
    billing_cycle: str = Field(min_length=4, max_length=8, default='monthly')
    status: str = Field(default='active')
    
    @field_validator('price')
    def price_positive(cls,v):
        if v < 0:
            raise ValueError('The price must be positive')
        return v
    
    @field_validator('billing_cycle')
    def valid_billing_cycle(cls, v):
        if v not in  ['monthly', 'yearly']:
            raise ValueError('Billing cycle must be monthly or yearly')
        return v
    
    @field_validator('service_name')
    def valid_character_specials(cls, v):
        if not re.match(r'^[a-zA-Z0-9\s]+$', v):
            raise ValueError('Service name cannot contain special characters')
        return v