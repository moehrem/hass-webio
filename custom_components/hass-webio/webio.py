"""Contain all utilities for webIO integration."""

import logging
from aiohttp import ClientSession, ClientError

from homeassistant.helpers.update_coordinator import UpdateFailed

from .const import REQUEST_TIMEOUT

_LOGGER = logging.getLogger(__name__)


async def get_json_data(
    ip: str,
    session: ClientSession,
    password: str | None = None,
) -> None:
    """Fetch data from the WebIO device."""
    url = f"http://{ip}/rest/json"
    if password:
        url += f"?PW={password}"

    try:
        async with session.get(url, timeout=REQUEST_TIMEOUT) as response:
            if response.status != 200:
                raise UpdateFailed(f"Unexpected status code: {response.status}")
            return await response.json()
    except ClientError as err:
        raise UpdateFailed(f"Error fetching data: {err}") from err


async def post_output_state(
    ip: str,
    index: int,
    state: bool,
    session: ClientSession,
    password: str | None = None,
) -> None:
    """Send a POST request to switch output on the WebIO device."""
    value = "ON" if state else "OFF"
    url = f"http://{ip}/rest/json/iostate/output/{index}"
    if password:
        url += f"?PW={password}"

    try:
        async with session.post(
            url, data={"Set": value}, timeout=REQUEST_TIMEOUT
        ) as response:
            if response.status != 200:
                raise ClientError(
                    f"Failed to set output {index}: HTTP {response.status}"
                )
            _LOGGER.debug("Successfully set output %d to %s", index, value)
    except ClientError as err:
        _LOGGER.error("Error setting output %d: %s", index, err)
        raise
