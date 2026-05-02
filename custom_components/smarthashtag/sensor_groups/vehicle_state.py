"""Vehicle-state entity descriptions.

Sourced from pysmarthashtag's ``vehicle.state`` (``VehicleState``), which
parses the GetCarState endpoint (``/remote-control/vehicle/status/state/{vin}``).
These are the TBox-side flags Hello # uses to confirm command dispatch
(notably ``journalLogState`` — the trip-recording toggle).

This module exports two collections:

* ``ENTITY_VEHICLE_STATE_DESCRIPTIONS`` — multi-value / informational sensors
  (timestamps, mode enums, misc state codes).
* ``ENTITY_VEHICLE_STATE_BINARY_DESCRIPTIONS`` — boolean 0/1 flags as
  binary sensors. Each carries an ``is_on_fn`` lambda that maps the
  pysmarthashtag attribute to a HA bool.
"""

from __future__ import annotations

import dataclasses
from typing import Any, Callable

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
)


@dataclasses.dataclass(frozen=True, kw_only=True)
class SmartHashtagBinarySensorEntityDescription(BinarySensorEntityDescription):
    """A class that enhances Binary Sensor entities."""

    is_on_fn: Callable[[Any, str], bool]


# --- Multi-value sensors ----------------------------------------------------

ENTITY_VEHICLE_STATE_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="next_wakeup_time",
        translation_key="next_wakeup_time",
        name="Next TBox wakeup",
        icon="mdi:clock-outline",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        # Distinct key from the existing engine_state sensor (which renders the
        # string form from vehicle.engine_state); this one renders the int 0/1
        # from VehicleState.engine_state and has to dispatch off attribute name.
        key="engine_state_int",
        translation_key="engine_state_int",
        name="Engine state (int)",
        icon="mdi:engine",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="power_mode",
        translation_key="power_mode",
        name="Power mode",
        icon="mdi:car-key",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="svt_state",
        translation_key="svt_state",
        name="Stolen Vehicle Tracking state",
        icon="mdi:car-traction-control",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="pnc_status",
        translation_key="pnc_status",
        name="Plug-and-Charge status",
        icon="mdi:ev-plug-type2",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="vstd_state",
        translation_key="vstd_state",
        name="VSTD state",
        icon="mdi:numeric",
        entity_registry_enabled_default=False,
    ),
)


# --- Binary sensors ---------------------------------------------------------
# Each lambda receives (vehicle, key) and must return a bool.
# `vehicle.state` is the VehicleState dataclass; some flags may be None
# (the field wasn't present in the response) — we render those as False.

def _flag(attr_name: str, on_value: int = 1):
    """Build an is_on_fn that reads attr_name from vehicle.state and compares."""
    def fn(vehicle, _key):
        state = getattr(vehicle, "state", None)
        if state is None:
            return False
        v = getattr(state, attr_name, None)
        return v == on_value
    return fn


ENTITY_VEHICLE_STATE_BINARY_DESCRIPTIONS: tuple[SmartHashtagBinarySensorEntityDescription, ...] = (
    # The headline flag — the one Hello # toggles for trip recording
    SmartHashtagBinarySensorEntityDescription(
        key="journal_log_state",
        translation_key="trip_recording_active",
        name="Trip recording",
        icon="mdi:road-variant",
        is_on_fn=_flag("journal_log_state"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="position_upload_state",
        translation_key="position_upload_active",
        name="Position upload",
        icon="mdi:crosshairs-gps",
        is_on_fn=_flag("position_upload_state"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="car_locator_active",
        translation_key="car_locator_active",
        name="Car locator service",
        icon="mdi:map-marker-radius",
        entity_registry_enabled_default=False,
        is_on_fn=_flag("car_locator_active"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="valet_mode_state",
        translation_key="valet_mode_active",
        name="Valet mode",
        icon="mdi:account-tie",
        is_on_fn=_flag("valet_mode_state"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="privacy_mode",
        translation_key="privacy_mode_active",
        name="Privacy mode",
        icon="mdi:incognito",
        is_on_fn=_flag("privacy_mode"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="overheat_state",
        translation_key="cabin_overheat_protection_active",
        name="Cabin overheat protection",
        icon="mdi:thermometer-alert",
        device_class=BinarySensorDeviceClass.HEAT,
        is_on_fn=_flag("overheat_state"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="camping_mode_active",
        translation_key="camping_mode_active",
        name="Camping mode",
        icon="mdi:tent",
        entity_registry_enabled_default=False,
        is_on_fn=_flag("camping_mode_active"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="drift_mode_active",
        translation_key="drift_mode_active",
        name="Drift mode",
        icon="mdi:car-sports",
        entity_registry_enabled_default=False,
        is_on_fn=_flag("drift_mode_active"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="wash_car_mode_active",
        translation_key="wash_car_mode_active",
        name="Wash car mode",
        icon="mdi:car-wash",
        entity_registry_enabled_default=False,
        is_on_fn=_flag("wash_car_mode_active"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="chat_video_main_active",
        translation_key="chat_video_main_active",
        name="In-car video chat",
        icon="mdi:video",
        entity_registry_enabled_default=False,
        is_on_fn=_flag("chat_video_main_active"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="park_comfort_state",
        translation_key="park_comfort_state",
        name="Park comfort",
        icon="mdi:sofa",
        entity_registry_enabled_default=False,
        is_on_fn=_flag("park_comfort_state"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="pulse_heat_active",
        translation_key="pulse_heat_active",
        name="Battery pulse heating",
        icon="mdi:radiator",
        device_class=BinarySensorDeviceClass.HEAT,
        entity_registry_enabled_default=False,
        is_on_fn=_flag("pulse_heat_active"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="bt_active",
        translation_key="bt_active",
        name="Bluetooth main",
        icon="mdi:bluetooth",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_registry_enabled_default=False,
        is_on_fn=_flag("bt_active"),
    ),
    SmartHashtagBinarySensorEntityDescription(
        key="bt_temp_active",
        translation_key="bt_temp_active",
        name="Bluetooth temporary",
        icon="mdi:bluetooth-connect",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_registry_enabled_default=False,
        is_on_fn=_flag("bt_temp_active"),
    ),
)
