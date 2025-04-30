from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str

    # Genera __tablename__ automáticamente
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
