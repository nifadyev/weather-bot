import pytest
from os import environ
from constants.owm_api import OPENWEATHERMAP_REQUEST_TEMPLATE

from owm_api import render_api_request


def test_render_api_request(set_owm_api_env_variables):
    expected_request = OPENWEATHERMAP_REQUEST_TEMPLATE.format(
        api_key="fake_app_id", latitude="12.3456789", longitude="98.7654321"
    )

    assert render_api_request() == expected_request


@pytest.mark.parametrize(
    argnames=("env_variable_name"),
    argvalues=("OPENWEATHERMAP_API_KEY", "LATITUDE", "LONGITUDE"),
)
def test_render_api_request_raises_value_error(
    env_variable_name, set_owm_api_env_variables
):
    del environ[env_variable_name]

    with pytest.raises(
        ValueError, match=f"Env variable `{env_variable_name}` is missing or empty"
    ):
        render_api_request()
