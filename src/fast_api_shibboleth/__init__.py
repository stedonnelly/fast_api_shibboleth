"""Minimal FastAPI Shibboleth SAML Authentication Package.

Usage:
    from fast_api_shibboleth import create_saml_router

    app = FastAPI()
    app.include_router(create_saml_router("idp_metadata.xml"))
"""

from .auth import create_saml_router

__all__ = ["create_saml_router"]
