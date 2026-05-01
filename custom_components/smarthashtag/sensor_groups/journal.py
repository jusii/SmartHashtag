"""Trip journal sensor entity descriptions.

Surfaces the most recent trip from the vehicle's journal log, including
the cloud's server-side reverse-geocoded start/end addresses.
"""

from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)

ENTITY_JOURNAL_DESCRIPTIONS = (
    SensorEntityDescription(
        key="last_trip_start_address",
        translation_key="last_trip_start_address",
        name="Last trip start address",
        icon="mdi:map-marker-up",
    ),
    SensorEntityDescription(
        key="last_trip_end_address",
        translation_key="last_trip_end_address",
        name="Last trip end address",
        icon="mdi:map-marker-down",
    ),
    SensorEntityDescription(
        key="last_trip_distance",
        translation_key="last_trip_distance",
        name="Last trip distance",
        icon="mdi:road-variant",
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="km",
    ),
    SensorEntityDescription(
        key="last_trip_duration",
        translation_key="last_trip_duration",
        name="Last trip duration",
        icon="mdi:timer-outline",
        device_class=SensorDeviceClass.DURATION,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="s",
    ),
    SensorEntityDescription(
        key="last_trip_energy_consumption",
        translation_key="last_trip_energy_consumption",
        name="Last trip energy consumption",
        icon="mdi:lightning-bolt",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kWh",
    ),
    SensorEntityDescription(
        key="last_trip_avg_energy_consumption",
        translation_key="last_trip_avg_energy_consumption",
        name="Last trip avg energy consumption",
        icon="mdi:chart-line",
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kWh/100km",
    ),
    SensorEntityDescription(
        key="last_trip_avg_speed",
        translation_key="last_trip_avg_speed",
        name="Last trip avg speed",
        icon="mdi:speedometer-medium",
        device_class=SensorDeviceClass.SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="km/h",
    ),
    SensorEntityDescription(
        key="last_trip_max_speed",
        translation_key="last_trip_max_speed",
        name="Last trip max speed",
        icon="mdi:speedometer",
        device_class=SensorDeviceClass.SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="km/h",
    ),
    SensorEntityDescription(
        key="last_trip_regenerated_energy",
        translation_key="last_trip_regenerated_energy",
        name="Last trip regenerated energy",
        icon="mdi:battery-charging-medium",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kWh",
    ),
    SensorEntityDescription(
        key="last_trip_start_time",
        translation_key="last_trip_start_time",
        name="Last trip start time",
        icon="mdi:clock-start",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key="last_trip_end_time",
        translation_key="last_trip_end_time",
        name="Last trip end time",
        icon="mdi:clock-end",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key="total_trips",
        translation_key="total_trips",
        name="Total trips",
        icon="mdi:counter",
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
)
