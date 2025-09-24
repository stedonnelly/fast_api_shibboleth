"""Minimal XML SAML configuration loader."""

import os
import xml.etree.ElementTree as ET
from typing import Any


def get_saml_config(
    xml_file: str | None = None, base_url: str | None = None
) -> dict[str, Any]:
    """Load minimal SAML config from XML."""
    # Use environment variable if no xml_file provided
    if xml_file is None:
        xml_file = os.getenv("SAML_METADATA_XML", "idp_metadata.xml")

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get entity ID
    entity_id = root.get("entityID")

    # Get SSO URL
    sso_elem = root.find(".//{urn:oasis:names:tc:SAML:2.0:metadata}SingleSignOnService")
    sso_url = sso_elem.get("Location") if sso_elem is not None else None

    # Get certificate
    cert_elem = root.find(".//{http://www.w3.org/2000/09/xmldsig#}X509Certificate")
    cert = (
        cert_elem.text.strip().replace("\n", "").replace(" ", "")
        if cert_elem is not None and cert_elem.text is not None
        else None
    )

    return {
        "strict": False,
        "debug": False,
        "sp": {
            "entityId": base_url,
            "assertionConsumerService": {
                "url": f"{base_url}/saml/acs",
                "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST",
            },
            "NameIDFormat": "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
        },
        "idp": {
            "entityId": entity_id,
            "singleSignOnService": {
                "url": sso_url,
                "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect",
            },
            "x509cert": cert,
        },
    }
