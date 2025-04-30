from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.poliza import PolizaCreate, PolizaInDB
from app.crud.crud_poliza import create_poliza, get_polizas
from app.api import deps
from app.core.auth import get_current_user


router = APIRouter()

@router.get("/", response_model=list[PolizaInDB])
def listar_polizas(db: Session = Depends(deps.get_db), user: dict = Depends(get_current_user)):
    return get_polizas(db)

@router.post("/", response_model=PolizaInDB)
def crear_poliza(poliza: PolizaCreate, db: Session = Depends(deps.get_db)):
    return create_poliza(db, poliza)
