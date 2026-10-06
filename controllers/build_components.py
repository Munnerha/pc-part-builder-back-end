from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.build import BuildModel
from models.build_component import BuildComponentModel
from models.component import ComponentModel
from models.user import UserModel
from serializers.build_component import BuildComponentSchema, CreateBuildComponentSchema, UpdateBuildComponentSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.post("/builds/{build_id}/build_components", response_model=BuildComponentSchema, status_code=201)
def create_build_component(build_id: int, build_component: CreateBuildComponentSchema, db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)):
    db_build = db.query(BuildModel).filter(BuildModel.id == build_id).first()

    if not db_build:
        raise HTTPException(status_code=404, detail="Build not found")

    if db_build.user_id != user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    # the part must exist in the catalog
    component = db.query(ComponentModel).filter(ComponentModel.id == build_component.component_id).first()

    if not component:
        raise HTTPException(status_code=404, detail="Component not found")

    new_build_component = BuildComponentModel(**build_component.model_dump(), build_id=build_id)

    db.add(new_build_component)
    db.commit()
    db.refresh(new_build_component)

    return new_build_component

@router.put("/build_components/{build_component_id}", response_model=BuildComponentSchema)
def update_build_component(build_component_id: int, build_component: UpdateBuildComponentSchema, db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)):
    db_build_component = db.query(BuildComponentModel).filter(BuildComponentModel.id == build_component_id).first()

    if not db_build_component:
        raise HTTPException(status_code=404, detail="Build component not found")

    if db_build_component.build.user_id != user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    build_component_data = build_component.model_dump(exclude_unset=True)

    # only checked when the part is being swapped
    if "component_id" in build_component_data:
        component = db.query(ComponentModel).filter(ComponentModel.id == build_component_data["component_id"]).first()

        if not component:
            raise HTTPException(status_code=404, detail="Component not found")

    for key, value in build_component_data.items():
        setattr(db_build_component, key, value)

    db.commit()
    db.refresh(db_build_component)

    return db_build_component

@router.delete("/build_components/{build_component_id}", status_code=204)
def delete_build_component(build_component_id: int, db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)):
    db_build_component = db.query(BuildComponentModel).filter(BuildComponentModel.id == build_component_id).first()

    if not db_build_component:
        raise HTTPException(status_code=404, detail="Build component not found")

    if db_build_component.build.user_id != user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    db.delete(db_build_component)
    db.commit()

    return None