"""Climate entities for the Overkiz (by Somfy) integration."""
from pyoverkiz.enums.ui import UIWidget

from .domestic_hot_water_production import DomesticHotWaterProduction
from .hitachi_dhw import HitachiDHW


WIDGET_TO_WATER_HEATER_ENTITY = {
    UIWidget.DOMESTIC_HOT_WATER_PRODUCTION: DomesticHotWaterProduction,
    UIWidget.HITACHI_DHW: HitachiDHW,
}
