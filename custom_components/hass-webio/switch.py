"""Manage all switch instances of WebIO."""

from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import WebIOCoordinator
from .entity import WebIOBaseEntity
from .webio import post_output_state

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up WebIO switches (outputs) from a config entry."""
    coordinator: WebIOCoordinator = hass.data[DOMAIN][entry.entry_id]

    try:
        outputs = coordinator.data["iostate"]["output"]
    except KeyError:
        _LOGGER.warning("No output data found in WebIO response")
        return

    entities = [WebIOSwitch(coordinator, entry, idx) for idx in range(len(outputs))]

    async_add_entities(entities)


class WebIOSwitch(WebIOBaseEntity, SwitchEntity):
    """Representation of a WebIO output as a switch."""

    def __init__(
        self,
        coordinator: WebIOCoordinator,
        config_entry: ConfigEntry,
        index: int,
    ) -> None:
        """Initialize the switch entity."""
        super().__init__(coordinator, config_entry, index, "output")

        self._attr_name = self.custom_name
        self._attr_unique_id = (
            f"{self._devicename.lower().replace(' ', '_')}_{self.io_type}_{self.index}"
        )
        self.entity_id = f"sensor.{self._attr_unique_id}"

    @property
    def is_on(self) -> bool:
        """Return true if the output is ON."""
        return self.coordinator.data["iostate"]["output"][self.index]["state"] == 1

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the output ON via REST API."""
        await post_output_state(
            ip=self._ip,
            index=self.index,
            state=True,
            session=self.coordinator.session,
            password=self.coordinator.password,
        )
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the output OFF via REST API."""
        await post_output_state(
            ip=self._ip,
            index=self.index,
            state=False,
            session=self.coordinator.session,
            password=self.coordinator.password,
        )
        await self.coordinator.async_request_refresh()
