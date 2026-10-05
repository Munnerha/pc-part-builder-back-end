from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models.build import BuildModel
from models.user import UserModel
from serializers.build import BuildSchema, CreateBuildSchema, UpdateBuildSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/builds", response_model=List[BuildSchema])
def get_builds(db: Session = Depends(get_db)):
    builds = db.query(BuildModel).all()

    return builds

@router.get("/builds/{build_id}", response_model=BuildSchema)
def get_single_build(build_id: int, db: Session = Depends(get_db)):
    build = db.query(BuildModel).filter(BuildModel.id == build_id).first()

    if not build:
        raise HTTPException(status_code=404, detail="Build not found")

    return build

@router.post("/builds", response_model=BuildSchema, status_code=201)
def create_build(build: CreateBuildSchema, db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)):
    new_build = BuildModel(**build.model_dump(), user_id=user.id)

    db.add(new_build)
    db.commit()
    db.refresh(new_build)

    return new_build

@router.put("/builds/{build_id}", response_model=BuildSchema)
def update_build(build_id: int, build: UpdateBuildSchema, db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)):
    db_build = db.query(BuildModel).filter(BuildModel.id == build_id).first()

    if not db_build:
        raise HTTPException(status_code=404, detail="Build not found")

    if db_build.user_id != user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    build_data = build.model_dump(exclude_unset=True)

    for key, value in build_data.items():
        setattr(db_build, key, value)

    db.commit()
    db.refresh(db_build)

    return db_build

@router.delete("/builds/{build_id}", status_code=204)
def delete_build(build_id: int, db: Session = Depends(get_db), user: UserModel = Depends(get_current_user)):
    db_build = db.query(BuildModel).filter(BuildModel.id == build_id).first()

    if not db_build:
        raise HTTPException(status_code=404, detail="Build not found")

    # admins can delete any build
    if db_build.user_id != user.id and user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")

    db.delete(db_build)
    db.commit()

    return None