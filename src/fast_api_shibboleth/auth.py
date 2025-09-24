"""Minimal SAML authentication for FastAPI."""

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from onelogin.saml2.auth import OneLogin_Saml2_Auth  # type: ignore[import-untyped]

from .config_loader import get_saml_config


def create_saml_router(xml_file: str | None = None) -> APIRouter:
    """Create minimal SAML router with login and response handling."""
    router = APIRouter()

    @router.get("/login")
    async def saml_login(request: Request):
        """Redirect to IdP for SAML login."""
        base_url = f"{request.url.scheme}://{request.headers.get('host')}"
        settings = get_saml_config(xml_file, base_url)

        req = {
            "https": "on" if request.url.scheme == "https" else "off",
            "http_host": request.headers.get("host"),
            "server_port": "443" if request.url.scheme == "https" else "80",
            "script_name": request.url.path,
            "get_data": dict(request.query_params),
            "post_data": {},
        }

        auth = OneLogin_Saml2_Auth(req, settings)
        return RedirectResponse(url=auth.login())

    @router.post("/acs")
    async def saml_acs(request: Request):
        """Handle SAML response from IdP."""
        base_url = f"{request.url.scheme}://{request.headers.get('host')}"
        settings = get_saml_config(xml_file, base_url)

        req = {
            "https": "on" if request.url.scheme == "https" else "off",
            "http_host": request.headers.get("host"),
            "server_port": "443" if request.url.scheme == "https" else "80",
            "script_name": request.url.path,
            "get_data": dict(request.query_params),
            "post_data": await request.form(),
        }

        auth = OneLogin_Saml2_Auth(req, settings)
        auth.process_response()

        if auth.is_authenticated():
            return {
                "authenticated": True,
                "user": auth.get_nameid(),
                "attributes": auth.get_attributes(),
            }

        return {"authenticated": False, "errors": auth.get_errors()}

    return router
