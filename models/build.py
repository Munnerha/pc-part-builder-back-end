from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class BuildModel(BaseModel):

    __tablename__ = "builds"

    name = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("UserModel", back_populates="builds")
    build_components = relationship("BuildComponentModel", back_populates="build", cascade="all, delete-orphan")