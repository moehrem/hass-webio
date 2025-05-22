"""Manage all counter sensors of WebIO."""

from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity
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
    """Set up WebIO counter sensors from a config entry."""
    coordinator: WebIOCoordinator = hass.data[DOMAIN][entry.entry_id]

    try:
        counters = coordinator.data["iostate"]["counter"]
    except KeyError:
        _LOGGER.warning("No counter data found in WebIO response")
        return

    entities = [
        WebIOCounterSensor(coordinator, entry, idx) for idx in range(len(counters))
    ]

    async_add_entities(entities)


class WebIOCounterSensor(WebIOBaseEntity, SensorEntity):
    """Representation of a WebIO counter as a sensor."""

    def __init__(
        self,
        coordinator: WebIOCoordinator,
        config_entry: ConfigEntry,
        index: int,
    ) -> None:
        """Initialize the counter sensor."""
        super().__init__(coordinator, config_entry, index, "counter")

        self._attr_name = self.custom_name
        self._attr_unique_id = (
            f"{self._devicename.lower().replace(' ', '_')}_{self.io_type}_{self.index}"
        )
        self.entity_id = f"sensor.{self._attr_unique_id}"
        self._attr_native_unit_of_measurement = "pulses"
        self._attr_device_class = "none"

    @property
    def native_value(self) -> int:
        """Return the current value of the counter."""
        return self.coordinator.data["iostate"]["counter"][self.index]["state"]

    @property
    def icon(self) -> str:
        """Return icon for counter sensor."""
        return "mdi:counter"
