"""Coordinator for WebIO integration."""

import logging
from datetime import timedelta

from aiohttp import ClientSession, ClientError
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD

from .const import DOMAIN
from .webio import get_json_data

_LOGGER = logging.getLogger(__name__)


class WebIOCoordinator(DataUpdateCoordinator):
    """Coordinator to manage fetching WebIO data."""

    def __init__(
        self,
        hass: HomeAssistant,
        session: ClientSession,
        config_entry: ConfigEntry,
    ):
        """Initialize the WebIO coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN} Coordinator",
            update_interval=timedelta(seconds=5),
        )

        self.session = session
        self.ip_address = config_entry.data[CONF_IP_ADDRESS]
        self.password = config_entry.data.get(CONF_PASSWORD)  # kann None sein
        self.config_entry = config_entry

    async def _async_update_data(self):
        """Fetch data from the WebIO device."""
        return await get_json_data(
            ip=self.ip_address, session=self.session, password=self.password
        )
