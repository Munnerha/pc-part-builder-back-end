from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class BuildComponentModel(BaseModel):

    __tablename__ = "build_components"

    build_id = Column(Integer, ForeignKey("builds.id"), nullable=False)
    component_id = Column(Integer, ForeignKey("components.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    build = relationship("BuildModel", back_populates="build_components")
    component = relationship("ComponentModel")