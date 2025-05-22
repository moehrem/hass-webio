"""Initialize the webIO integration.

Konzept:
- Einrichtung mit IP und Passwort
- ggf automatische Erkennung der webIO-Instanz
- Abfrage per TCP/IP mit Polling

- initial Abfrage auf "allout"
- daraus ableitend die Anzahl der Eingänge und Ausgänge
- Erstellung eines Gerätes
- Anlage einer entsprechenden Anzahl von Sensoren und Schaltern

- Änderung der Schalter in HA muss an webIO weitergegeben werden
- Änderung nur für Outputs zulässig
- Inputs werden nur gelesen, nicht geschrieben


"""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN
from .coordinator import WebIOCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["binary_sensor", "sensor", "switch"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up WebIO from a config entry."""
    _LOGGER.debug("Setting up WebIO entry")

    session = async_get_clientsession(hass)

    coordinator = WebIOCoordinator(
        hass=hass,
        session=session,
        config_entry=entry,
    )

    await coordinator.async_config_entry_first_refresh()

    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_get_options_flow(config_entry):
    from .options_flow import WebIOOptionsFlowHandler

    return WebIOOptionsFlowHandler(config_entry)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok and DOMAIN in hass.data:
        hass.data[DOMAIN].pop(entry.entry_id, None)

    return unload_ok
