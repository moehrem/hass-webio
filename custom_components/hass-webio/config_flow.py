"""Config flow to configure the WebIO device."""

import logging
from typing import Any

import voluptuous as vol
from aiohttp import ClientError

from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class WebIOConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for the WebIO integration."""

    def __init__(self) -> None:
        self._ip: str | None = None
        self._password: str | None = None
        self._inputs: int = 0
        self._outputs: int = 0
        self._session = None
        self._errors: dict[str, str] = {}
        self._input_names: dict[str, str] = {}

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial user step (IP + optional password)."""
        if user_input is not None:
            self._ip = user_input[CONF_IP_ADDRESS]
            self._password = user_input.get(CONF_PASSWORD) or None
            self._session = async_get_clientsession(self.hass)

            url = f"http://{self._ip}/rest/json"
            if self._password:
                url += f"?PW={self._password}"

            try:
                async with self._session.get(url, timeout=5) as response:
                    if response.status != 200:
                        raise ClientError(f"Invalid response code: {response.status}")
                    data = await response.json()
                    self._inputs = len(data["iostate"]["input"])
                    self._outputs = len(data["iostate"]["output"])
            except Exception as e:
                _LOGGER.error("Connection to WebIO failed: %s", e)
                self._errors["base"] = "cannot_connect"
                return self._show_user_form()

            return await self.async_step_inputs()

        return self._show_user_form()

    def _show_user_form(self) -> ConfigFlowResult:
        """Show the initial form to collect IP and password."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_IP_ADDRESS): str,
                    vol.Optional(CONF_PASSWORD, default=""): str,
                }
            ),
            errors=self._errors,
        )

    async def async_step_inputs(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Step to name input channels."""
        if user_input is not None:
            self._input_names = user_input
            return await self.async_step_outputs()

        fields = {
            vol.Optional(f"input_name_{i}", default=f"Input {i}"): str
            for i in range(self._inputs)
        }

        return self.async_show_form(
            step_id="inputs",
            data_schema=vol.Schema(fields),
        )

    async def async_step_outputs(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Step to name output channels."""
        if user_input is not None:
            # Combine inputs + outputs + device data
            data = {
                CONF_IP_ADDRESS: self._ip,
            }
            if self._password:
                data[CONF_PASSWORD] = self._password

            data.update(self._input_names)
            data.update(user_input)

            return self.async_create_entry(
                title=f"WebIO @ {self._ip}",
                data=data,
            )

        fields = {
            vol.Optional(f"output_name_{i}", default=f"Output {i}"): str
            for i in range(self._outputs)
        }

        return self.async_show_form(
            step_id="outputs",
            data_schema=vol.Schema(fields),
        )
