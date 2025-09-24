"""Minimal SAML authentication example."""

from fastapi import FastAPI

from fast_api_shibboleth import create_saml_router

app = FastAPI()

# Add SAML auth routes - that's it!
app.include_router(create_saml_router())

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
