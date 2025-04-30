from sqlalchemy import Column, String, Integer, Date, Float
from app.db.base_class import Base

class Poliza(Base):
    __tablename__ = "Polizas"

    numero_poliza = Column("NumeroPoliza", String, primary_key=True, index=True)
    tipo_poliza_id = Column("TipoPolizaid", Integer)
    cedula_asegurado = Column("CedulaAsegurado", String)
    monto_asegurado = Column("MontoAsegurado", Float)
    fecha_vencimiento = Column("FechaVencimiento", Date)
    fecha_emision = Column("FechaEmision", Date)
    cobertura_id = Column("CoberturaId", Integer)
    estado_poliza_id = Column("EstadoPolizaId", Integer)
    prima = Column("Prima", Float)
    periodo = Column("Periodo", Date)
    fecha_inclusion = Column("FechaInclusion", Date)
    aseguradora_id = Column("AseguradoraId", Integer)
