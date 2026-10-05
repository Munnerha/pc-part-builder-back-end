from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from models.component import ComponentModel
from serializers.component import ComponentSchema
from database import get_db

router = APIRouter()

@router.get("/components", response_model=List[ComponentSchema])
def get_components(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(ComponentModel)

    if category:
        query = query.filter(ComponentModel.category == category)

    return query.all()