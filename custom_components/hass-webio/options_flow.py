import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD
from homeassistant.helpers.aiohttp_client import async_get_clientsession


_LOGGER = logging.getLogger(__name__)


class WebIOOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle WebIO options."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry
        self._ip = config_entry.data[CONF_IP_ADDRESS]
        self._password = config_entry.data[CONF_PASSWORD]
        self._inputs = 0
        self._outputs = 0
        self._session = None

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Manage the WebIO options."""
        self._session = async_get_clientsession(self.hass)

        # Lade aktuelle Kanalanzahl
        try:
            url = f"http://{self._ip}/rest/json?PW={self._password}"
            async with self._session.get(url, timeout=5) as response:
                data = await response.json()
                self._inputs = len(data["iostate"]["input"])
                self._outputs = len(data["iostate"]["output"])
        except Exception as e:
            _LOGGER.error("Failed to load WebIO state for options: %s", e)
            return self.async_abort(reason="cannot_connect")

        return await self._show_form(user_input)

    async def _show_form(
        self, user_input: dict[str, Any] | None
    ) -> config_entries.ConfigFlowResult:
        """Show the options form."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        fields = {}
        for i in range(self._inputs):
            default = (
                self.config_entry.options.get(f"input_name_{i}")
                or self.config_entry.data.get(f"input_name_{i}")
                or f"Input {i}"
            )
            fields[vol.Optional(f"input_name_{i}", default=default)] = str

        for i in range(self._outputs):
            default = (
                self.config_entry.options.get(f"output_name_{i}")
                or self.config_entry.data.get(f"output_name_{i}")
                or f"Output {i}"
            )
            fields[vol.Optional(f"output_name_{i}", default=default)] = str

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(fields),
        )
