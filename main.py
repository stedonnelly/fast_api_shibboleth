"""Minimal SAML authentication example."""

import os

from dotenv import load_dotenv
from fastapi import FastAPI

from fast_api_shibboleth import create_saml_router

load_dotenv("./.env")  # Load environment variables from .env file

if os.environ.get("SAML_METADATA_XML") is None:
    err_string = "SAML_METADATA_XML environment variable not set"
    raise ValueError(err_string)
else:
    print(f"SAML_METADATA_XML is set to: {os.environ.get('SAML_METADATA_XML')}")

app = FastAPI()

# Add SAML auth routes - that's it!
app.include_router(create_saml_router())

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
