# fast_api_shibboleth

[![Actions Status][actions-badge]][actions-link]
[![PyPI version][pypi-version]][pypi-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

A package for integrating shibboleth SSO into a FastAPI instance

## Installation

From source:
```bash
git clone https://github.com/stedonnelly/fast_api_shibboleth
cd fast_api_shibboleth
python -m pip install .
```

## Usage

This repo comes with a `main.py` file that can be used to demonstrate and test your SAML login flow. This uses an xml first approach to handling the configuration. This can be configured by either passing an absolute path to the `create_saml_router` function or setting the `SAML_METADATA_XML` environment variable to the path of the xml file.

### Environment Variables

Create the `.env` file from the `.env.example`.

```bash
cp .env.example .env
```

Example .env file:
```
SAML_METADATA_XML=/app/metadata/saml_metadata.xml
```

### Running the test server

```bash
python main.py
```

You can then test your saml login route by navigating to http://localhost:8000/auth/saml/login.

### Optional configuration

You can optionally configure the login and ACS routes by setting the following environment variables.
```
SAML_LOGIN_ROUTE=/custom/route/login # Defaults to /auth/saml/login if not set
SAML_ACS_ROUTE=/custom/route/acs # Defaults to /auth/saml/acs if not set
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to contribute.

## License

Distributed under the terms of the [MIT license](LICENSE).


<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/stedonnelly/fast_api_shibboleth/workflows/CI/badge.svg
[actions-link]:             https://github.com/stedonnelly/fast_api_shibboleth/actions
[pypi-link]:                https://pypi.org/project/fast_api_shibboleth/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/fast_api_shibboleth
[pypi-version]:             https://img.shields.io/pypi/v/fast_api_shibboleth
<!-- prettier-ignore-end -->
