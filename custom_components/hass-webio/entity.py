"""Entity classes for wwebIO integration."""

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER
from .coordinator import WebIOCoordinator


class WebIOBaseEntity(CoordinatorEntity[WebIOCoordinator], Entity):
    """Base entity for all WebIO sensors/switches."""

    def __init__(
        self,
        coordinator: WebIOCoordinator,
        config_entry: ConfigEntry,
        index: int,
        io_type: str,  # "input", "output", "counter"
    ) -> None:
        """Initialize the base entity."""
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.index = index
        self.io_type = io_type  # for name lookup
        self._ip = coordinator.ip_address
        self._devicename = self.coordinator.data["info"]["devicename"]

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device info to group all entities under one device."""
        return {
            "identifiers": {(DOMAIN, self._ip)},
            "name": f"WebIO @ {self._ip}",
            "manufacturer": MANUFACTURER,
            "model": self._devicename,
            # "sw_version": "REST API",
        }

    @property
    def custom_name(self) -> str:
        """Get custom name for this entity."""
        # Sonderfall: Counter sollen den Namen des zugehörigen Eingangs übernehmen
        name_key = (
            f"input_name_{self.index}"
            if self.io_type == "counter"
            else f"{self.io_type}_name_{self.index}"
        )

        return (
            self.config_entry.options.get(name_key)
            or self.config_entry.data.get(name_key)
            or f"{self.io_type.capitalize()} {self.index}"
        )
