from fastapi import Depends, FastAPI

from .guard import verify_request_credentials

app = FastAPI(title="agd-request-guard demo")

_QUEUE_STATE = {"position": 4, "dispatch_token": "QT-88213-INTERNAL"}


@app.get("/public/status")
def public_status():
    return {"ok": True}


@app.get("/internal/queue-state", dependencies=[Depends(verify_request_credentials)])
def queue_state():
    return _QUEUE_STATE


@app.patch("/internal/queue-state", dependencies=[Depends(verify_request_credentials)])
def update_queue_state(payload: dict):
    _QUEUE_STATE.update(payload)
    return _QUEUE_STATE
