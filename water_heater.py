"""Support for Overkiz WATER_HEATER devices."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import HomeAssistantOverkizData
from .water_heater_entities import WIDGET_TO_WATER_HEATER_ENTITY
from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Overkiz WATER_HEATER from a config entry."""
    data: HomeAssistantOverkizData = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        WIDGET_TO_WATER_HEATER_ENTITY[device.widget](device.device_url, data.coordinator)
        for device in data.platforms[Platform.WATER_HEATER]
        if device.widget in WIDGET_TO_WATER_HEATER_ENTITY
    )