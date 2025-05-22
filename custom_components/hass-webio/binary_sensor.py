"""Manage all binary sensors for WebIO."""

from __future__ import annotations

import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import WebIOCoordinator
from .entity import WebIOBaseEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up WebIO binary sensors (inputs) from a config entry."""
    coordinator: WebIOCoordinator = hass.data[DOMAIN][entry.entry_id]

    try:
        inputs = coordinator.data["iostate"]["input"]
    except KeyError:
        _LOGGER.warning("No input data found in WebIO response")
        return

    entities = [WebIOBinaryInput(coordinator, entry, idx) for idx in range(len(inputs))]

    async_add_entities(entities)


class WebIOBinaryInput(WebIOBaseEntity, BinarySensorEntity):
    """Representation of a WebIO digital input."""

    def __init__(
        self,
        coordinator: WebIOCoordinator,
        config_entry: ConfigEntry,
        index: int,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator, config_entry, index, "input")

        self._attr_name = self.custom_name
        self._attr_unique_id = (
            f"{self._devicename.lower().replace(' ', '_')}_{self.io_type}_{self.index}"
        )
        self.entity_id = f"sensor.{self._attr_unique_id}"
        self._attr_device_class = "power"  # ggf. anpassen: "occupancy", "motion", ...

    @property
    def is_on(self) -> bool:
        """Return true if the input is high."""
        return self.coordinator.data["iostate"]["input"][self.index]["state"] == 1
