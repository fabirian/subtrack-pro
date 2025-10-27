from sqlalchemy import Column, Integer, String, Float, Date, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Subscription(Base):
    __tablename__ = "subscriptions"
    id= Column(Integer, primary_key=True, index=True)
    user_id= Column(Integer, ForeignKey("users.id"), nullable= False)
    service_name= Column(String, nullable=False)
    plan_name= Column(String)
    price= Column(Float, nullable= False)
    renewal_date= Column(Date, nullable= False)
    billing_cycle= Column(String, nullable= False, default= 'monthly')
    category_id= Column(Integer, ForeignKey("categories.id"))
    status= Column(String, default= 'active')
    created_at= Column(TIMESTAMP, server_default=func.now())
    
    user = relationship("User", back_populates="subscriptions")
    category = relationship("Category", back_populates="subscriptions")
    payments = relationship("Payment", back_populates="subscription")