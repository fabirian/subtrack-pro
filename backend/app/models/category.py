from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String, nullable=False, unique=True)
    description= Column(String)
    created_at= Column(TIMESTAMP, server_default=func.now())
    
    subscriptions = relationship("Subscription", back_populates="category")