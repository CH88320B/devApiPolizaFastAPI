from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from urllib.request import urlopen
import json
from app.core.config import settings

http_bearer = HTTPBearer()

def verify_jwt(token: str):
    jwks_url = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"
    with urlopen(jwks_url) as response:
        jwks = json.load(response)

    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=settings.AUTH0_ALGORITHMS,
                audience=settings.AUTH0_API_AUDIENCE,
                issuer=f"https://{settings.AUTH0_DOMAIN}/"
            )
            return payload
        except Exception as e:
            raise HTTPException(status_code=401, detail="Token inválido")
    raise HTTPException(status_code=401, detail="No se pudo verificar token")

def get_current_user(token: HTTPAuthorizationCredentials = Depends(http_bearer)):
    return verify_jwt(token.credentials)
