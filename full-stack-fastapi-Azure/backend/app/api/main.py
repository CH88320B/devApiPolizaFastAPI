from fastapi import APIRouter
from app.api.api_v1.endpoints import poliza  # solo poliza (sin la 's')

from app.core.config import settings

api_router = APIRouter()

# Solo incluir polizas (correctamente importado como poliza.router)
api_router.include_router(poliza.router, prefix="/polizas", tags=["polizas"])
