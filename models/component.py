from sqlalchemy import Column, Integer, String, Float
from .base import BaseModel

class ComponentModel(BaseModel):

    __tablename__ = "components"

    category = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # only filled for the categories they apply to
    socket = Column(String)
    memory_type = Column(String)
    form_factor = Column(String)
    gpu_length = Column(Integer)
    max_gpu_length = Column(Integer)
    cooler_height = Column(Integer)
    max_cooler_height = Column(Integer)