from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    login: str = Field(primary_key=True)
    contrasena: str
