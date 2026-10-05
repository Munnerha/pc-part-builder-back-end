from pydantic import BaseModel
from typing import Optional
from .component import ComponentSchema

class BuildComponentSchema(BaseModel):
    id: int
    quantity: int
    component: ComponentSchema

    class Config:
        from_attributes = True

class CreateBuildComponentSchema(BaseModel):
    component_id: int
    quantity: int = 1

class UpdateBuildComponentSchema(BaseModel):
    component_id: Optional[int] = None
    quantity: Optional[int] = None