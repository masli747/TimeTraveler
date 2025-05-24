-- # Master Record View (for aggregations and exporting)

CREATE VIEW v_master_records AS
SELECT DISTINCT Trip.tripID, Trip.location, Trip.date AS trip_date,
       Trip.imageFile, Traveler.travelerID as TravelerID,
       Traveler.name AS traveler_name, Traveler.age AS traveler_age,
       Traveler.birthLocation AS traveler_origin,
       Traveler.currentTimePeriod AS traveler_time_period,
       Companion.companionID AS companion_id,
       Companion.companionID, Companion.name AS companion_name,
       Companion.age AS companion_age,
       Companion.originalLocation AS companion_origin,
       Companion.currentTimePeriod AS companion_time_period,
       Tool.toolID AS tool_id, Tool.name AS tool_name,
       Tool.powerCapacity AS tool_power_capacity,
       ToolAbility.toolAbilityID AS tool_ability_id,
       ToolAbility.name AS tool_ability_name,
       ToolAbility.description AS tool_ability_description,
       ToolAbility.powerConsumption AS tool_ability_power_consumption,
       toolAbility.successProbability AS tool_ability_success,
       Vehicle.vehicleID AS vehicle_id,
       Vehicle.name AS vehicle_name,
       Vehicle.powerCapacity AS vehicle_power_capacity,
       Vehicle.engine AS vehicle_engine,
       VehicleAbility.vehicleAbilityID AS vehicle_ability_id,
       VehicleAbility.name AS vehicle_ability_name,
       VehicleAbility.description AS vehicle_ability_description,
       VehicleAbility.powerConsumption AS vehicle_ability_power_consumption,
       VehicleAbility.successProbability AS vehicle_ability_success
FROM Trip
LEFT OUTER JOIN Traveler
ON Traveler.travelerID = Trip.travelerID
LEFT OUTER JOIN Companion
ON Companion.travelerID = Traveler.travelerID
LEFT OUTER JOIN Tool
ON Tool.travelerID = Traveler.travelerID
LEFT OUTER JOIN ToolAbility
ON Tool.toolID = ToolAbility.toolID
LEFT OUTER JOIN Vehicle
ON Vehicle.travelerID = Traveler.travelerID
LEFT OUTER JOIN VehicleAbility
ON Vehicle.vehicleID = VehicleAbility.vehicleID;

-- # View all data from view!
-- SELECT * FROM v_master_records;

-- # Deletion (in case)
-- DROP VIEW v_master_records;

-- # Indexes

CREATE INDEX name_index ON Traveler (name);
CREATE INDEX name_index ON Companion (name);