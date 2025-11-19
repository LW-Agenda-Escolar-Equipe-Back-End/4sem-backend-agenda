from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from ..database import get_db
from .. import crud, models, schemas


# Router config
router = APIRouter(
    prefix="/disciplinas",
    tags=["Disciplinas"],
    responses={404: {"description": "Not found"}},
)


# Endpoints

# Buscar disciplina por meio do ID
@router.get("/{discipline_id}", response_model=schemas.GenericResponse[schemas.Disciplina])
def get_discipline(discipline_id: int, db: Session = Depends(get_db)):
    discipline = crud.obter_disciplina(db, discipline_id)
    if not discipline:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return schemas.GenericResponse(
        data=discipline,
        success=True,
        message="Disciplina retornada com sucesso"
    )

# Listar todas as disciplinas
@router.get("/", response_model=schemas.GenericResponse[list[schemas.Disciplina]])
def get_all_disciplines(db: Session = Depends(get_db)):
    disciplinas = crud.listar_disciplinas(db)
    return schemas.GenericResponse(
        data=disciplinas,
        success=True,
        message="Disciplinas retornadas com sucesso"
    )


# Criar uma nova disciplina
@router.post("/", response_model=schemas.GenericResponse[schemas.Disciplina], status_code=201)
def create_discipline(disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    nova_disciplina = crud.criar_disciplina(db, disciplina)

    return schemas.GenericResponse(
        data=nova_disciplina,
        success=True,
        message="Disciplina criada com sucesso"
    )