# WebApiPolizasPython

Una API RESTful construida con **FastAPI** y **Python 3.11+**, conectada a una base de datos **Azure SQL Server**, con autenticación JWT utilizando **Auth0**, siguiendo buenas prácticas de arquitectura de proyectos modernos.

---

## 🚀 Tecnologías utilizadas

- **FastAPI**: Framework moderno para construir APIs con Python.
- **SQLModel / SQLAlchemy**: ORM para mapeo de datos a objetos.
- **Auth0**: Proveedor de autenticación JWT con OAuth 2.0.
- **Azure SQL Database**: Base de datos relacional en la nube.
- **Pydantic v2**: Validación de datos y esquemas de serialización.
- **Uvicorn**: Servidor ASGI para correr FastAPI.
- **Docker (opcional)**: Para ambientes productivos y despliegue.

---

## 🌟 Estructura del proyecto

```
backend/
├── app/
│   ├── api/
│   │   ├── api_v1/
│   │   │   └── endpoints/
│   │   │       └── poliza.py       # Endpoints REST de pólizas
│   │   └── main.py          # Define rutas globales
│   ├── core/
│   │   ├── config.py        # Configuraciones globales (.env)
│   │   ├── db.py            # Conexion a base de datos
│   │   └── auth.py          # Validación JWT con Auth0
│   ├── crud/
│   │   └── crud_poliza.py   # Acceso a datos
│   ├── models/
│   │   └── poliza.py        # Modelo ORM
│   ├── schemas/
│   │   └── poliza.py        # Esquemas Pydantic
│   └── main.py           # Punto de entrada principal
.env
requirements.txt
```

---

## ⚙️ Instalación y configuración local

### 1. Clonar el repositorio
```bash
git clone https://github.com/usuario/webapipolizas-python.git
cd webapipolizas-python/backend
```

### 2. Crear entorno virtual
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crear archivo `.env` basado en el ejemplo:
```env
ENVIRONMENT=local
PROJECT_NAME=WebApiPolizasPython
FRONTEND_HOST=http://localhost:5173

# Azure SQL
AZURE_SQL_SERVER=xxxx.database.windows.net
AZURE_SQL_USER=xxxxx
AZURE_SQL_PASSWORD=xxxxx
AZURE_SQL_DATABASE=DBPolizas
AZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server

# Auth0
AUTH0_DOMAIN=dev-xxxxxx.us.auth0.com
AUTH0_API_AUDIENCE=https://fastapi-api
AUTH0_ALGORITHMS=RS256
```

### 5. Correr la aplicación
```bash
uvicorn app.main:app --reload
```
Visita: `http://localhost:8000/docs`

---

## 🔐 Autenticación con Auth0

1. Crear cuenta en [Auth0](https://auth0.com/)
2. Crear una nueva API con identificador: `https://fastapi-api`
3. En **Applications**, registrar una SPA o Backend app:
   - Callback URL: `http://localhost:8000/docs`
   - Permitir `RS256` como algoritmo.
4. Copiar el `Domain` y `Client ID` al `.env`

**Protección de endpoints**
```python
from app.core.auth import get_current_user

@router.get("/", dependencies=[Depends(get_current_user)])
def listar():
    return servicio.listar()
```

---

## 🪖 Buenas prácticas aplicadas

- ✅ Separación de capas: `models`, `schemas`, `crud`, `api`, `core`
- ✅ Validación fuerte con **Pydantic v2**
- ✅ Protección JWT con validación desde Auth0 (sin claves locales)
- ✅ Variables sensibles en `.env`
- ✅ Uso de `Depends()` para inyección de dependencias
- ✅ Tipado estricto (Python 3.11+)

---

## 📊 Endpoints disponibles

| Método | Ruta                        | Protegido | Descripción                     |
|--------|-----------------------------|-----------|----------------------------------|
| GET    | `/api/v1/polizas/`          | ✅        | Lista todas las pólizas          |
| POST   | `/api/v1/polizas/`          | ✅        | Crear una nueva póliza           |

---

## 🚫 Errores comunes y soluciones

- **401 Token inválido**:
  - Verifica que el JWT esté bien formateado y sin comillas dobles.
  - Debe tener el `aud` igual al `AUTH0_API_AUDIENCE`.

- **Invalid column name**:
  - Verifica que los nombres en tu modelo `Poliza` coincidan exactamente con los de Azure SQL.

- **ModuleNotFoundError**:
  - Ejecuta `pip install -r requirements.txt` en el entorno correcto.

---

## 👨‍💻 Autor
**Henderson J. Castañeda S.**  
Ingeniero de Software | Cloud & API Developer

GitHub: [CH88320B](https://github.com/CH88320B)


