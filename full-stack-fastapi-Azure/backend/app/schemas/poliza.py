from datetime import date
from pydantic import BaseModel, Field

class PolizaBase(BaseModel):
    tipo_poliza_id: int = Field(alias="TipoPolizaId")
    cedula_asegurado: str = Field(alias="CedulaAsegurado")
    monto_asegurado: float = Field(alias="MontoAsegurado")
    fecha_vencimiento: date = Field(alias="FechaVencimiento")
    fecha_emision: date = Field(alias="FechaEmision")
    cobertura_id: int = Field(alias="CoberturaId")
    estado_poliza_id: int = Field(alias="EstadoPolizaId")
    prima: float = Field(alias="Prima")
    periodo: date = Field(alias="Periodo")
    fecha_inclusion: date = Field(alias="FechaInclusion")
    aseguradora_id: int = Field(alias="AseguradoraId")

class PolizaCreate(PolizaBase):
    numero_poliza: str = Field(alias="NumeroPoliza")

class PolizaInDB(PolizaBase):
    numero_poliza: str = Field(alias="NumeroPoliza")

    class Config:
        from_attributes = True  # Pydantic v2+
        populate_by_name = True  # permite usar los nombres externos
