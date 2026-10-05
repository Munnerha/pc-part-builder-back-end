from pydantic import BaseModel
from typing import Optional, List
from .user import UserSchema
from .build_component import BuildComponentSchema

class BuildSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    user: UserSchema
    build_components: List[BuildComponentSchema]

    class Config:
        from_attributes = True

class CreateBuildSchema(BaseModel):
    name: str
    description: Optional[str] = None

class UpdateBuildSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None