from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from devices.tracker import get_active_devices
import logging

app = FastAPI()
security = HTTPBearer()

API_TOKEN = "secret-token"  # Should come from secure config/env

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_TOKEN:
        logging.warning("Unauthorized access attempt")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token"
        )
    return True

@app.get("/devices")
def devices_list(auth: bool = Depends(verify_token)):
    devices = get_active_devices()
    return devices

# To run:
# uvicorn api.rest:app --host 0.0.0.0 --port 8080
