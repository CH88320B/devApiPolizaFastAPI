from typing import List, Optional
from sqlmodel import Session, select

from app.models.poliza import Poliza
from app.schemas.poliza import PolizaCreate, PolizaInDB

def create_poliza(db: Session, poliza: PolizaCreate) -> Poliza:
    db_poliza = Poliza.from_orm(poliza)
    db.add(db_poliza)
    db.commit()
    db.refresh(db_poliza)
    return db_poliza

def get_polizas(db: Session) -> List[Poliza]:
    return db.exec(select(Poliza)).all()

def get_poliza(db: Session, poliza_id: str) -> Optional[Poliza]:
    return db.exec(select(Poliza).where(Poliza.numero_poliza == poliza_id)).first()

def delete_poliza(db: Session, poliza_id: str) -> None:
    poliza = db.exec(select(Poliza).where(Poliza.numero_poliza == poliza_id)).first()
    if poliza:
        db.delete(poliza)
        db.commit()
