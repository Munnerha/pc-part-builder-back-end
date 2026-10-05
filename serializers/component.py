from pydantic import BaseModel
from typing import Optional

class ComponentSchema(BaseModel):
    id: int
    category: str
    brand: str
    name: str
    price: float
    socket: Optional[str] = None
    memory_type: Optional[str] = None
    form_factor: Optional[str] = None
    gpu_length: Optional[int] = None
    max_gpu_length: Optional[int] = None
    cooler_height: Optional[int] = None
    max_cooler_height: Optional[int] = None

    class Config:
        from_attributes = True