import os

from fastapi import Header, HTTPException

REQUEST_GUARD_KEY = os.getenv("REQUEST_GUARD_KEY", "")


def verify_request_credentials(x_api_key: str = Header(None)) -> str:
    """Require a valid API key for privileged routes."""
    if not x_api_key or not x_api_key.strip():
        raise HTTPException(status_code=401, detail="Missing credentials")
    return x_api_key
