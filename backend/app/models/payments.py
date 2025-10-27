from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = "payments"
    id= Column(Integer, primary_key=True, index=True)
    subscription_id= Column(Integer, ForeignKey("subscriptions.id"), nullable=False)
    amount= Column(Float, nullable=False)
    payment_date= Column(TIMESTAMP, server_default=func.now())
    status= Column(String, default='completed')
    
    subscription = relationship("Subscription", back_populates="payments")