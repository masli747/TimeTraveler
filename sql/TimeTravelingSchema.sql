CREATE SCHEMA IF NOT EXISTS TimeTravelingSchema;
USE TimeTravelingSchema;


-- Create tables
CREATE TABLE Traveler
(
    travelerID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    age int UNSIGNED NOT NULL DEFAULT 18,
    birthLocation VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    currentTimePeriod datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Companion
(
    companionID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    age int UNSIGNED NOT NULL DEFAULT 18,
    originalLocation VARCHAR(100) DEFAULT 'Unknown',
    currentTimePeriod datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,

    travelerID int UNSIGNED,
    FOREIGN KEY (travelerID) REFERENCES Traveler(travelerID)
);


CREATE TABLE Trip
(
    tripID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    -- POTENTIALLY CHANGE THIS
    imageFile VARCHAR(1000) NOT NULL DEFAULT 'Unknown',
    --
    travelerID int UNSIGNED,
    FOREIGN KEY (travelerID) REFERENCES Traveler(travelerID)
);

CREATE TABLE Tool
(
    toolID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    powerCapacity int NOT NULL DEFAULT 100,

    travelerID int UNSIGNED,
    FOREIGN KEY (travelerID) REFERENCES Traveler(travelerID)
);

CREATE TABLE ToolAbility
(
    toolAbilityID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    description VARCHAR(750) NOT NULL DEFAULT 'Unknown',
    powerConsumption int NOT NULL DEFAULT 10,

    successProbability int NOT NULL DEFAULT 50,
    CONSTRAINT restrict_toolAbilityProbability CHECK (successProbability BETWEEN 1 AND 100),

    toolID int UNSIGNED,
    FOREIGN KEY (toolID) REFERENCES Tool(toolID)
);

CREATE TABLE Vehicle
(
    vehicleID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    powerCapacity int NOT NULL DEFAULT 100,
    engine VARCHAR(100) NOT NULL DEFAULT 'Unknown',

    travelerID int UNSIGNED,
    FOREIGN KEY (travelerID) REFERENCES Traveler(travelerID)
);

CREATE TABLE VehicleAbility
(
    vehicleAbilityID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL DEFAULT 'Unknown',
    description VARCHAR(750) NOT NULL DEFAULT 'Unknown',
    powerConsumption int NOT NULL DEFAULT 10,

    successProbability int NOT NULL DEFAULT 50,
    CONSTRAINT restrict_vehicleAbilityProbability CHECK (successProbability BETWEEN 1 AND 100),

    vehicleID int UNSIGNED,
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID)
);



-- -- DEFAULT TEST VALUES
-- Insert into Traveler
INSERT INTO Traveler (name, age, birthLocation, currentTimePeriod)
VALUES
    ('John Doe', 30, 'Earth', '2023-10-01 12:00:00'),
    ('Alice Johnson', 25, 'Venus', '2023-10-02 14:00:00'),
    ('Bob Brown', 40, 'Mars', '2023-10-03 16:00:00');

-- Insert into Companion
INSERT INTO Companion (name, age, originalLocation, currentTimePeriod, travelerID)
VALUES
    ('Jane Smith', 28, 'Mars', '2023-10-01 12:00:00', 1),
    ('Emily Davis', 22, 'Jupiter', '2023-10-02 14:00:00', 2),
    ('Michael Lee', 35, 'Saturn', '2023-10-03 16:00:00', 3);

-- Insert into Trip
INSERT INTO Trip (location, date, imageFile, travelerID)
VALUES
    ('Ancient Rome', '2023-10-01 12:00:00', 'rome.jpg', 1),
    ('Medieval England', '2023-10-02 14:00:00', 'england.jpg', 2),
    ('Future Mars', '2023-10-03 16:00:00', 'mars.jpg', 3);

-- Insert into Tool
INSERT INTO Tool (name, powerCapacity, travelerID)
VALUES
    ('Time Watch', 200, 1),
    ('Quantum Compass', 150, 2),
    ('Temporal Scanner', 300, 3);

-- Insert into ToolAbility
INSERT INTO ToolAbility (name, description, powerConsumption, successProbability, toolID)
VALUES
    ('Time Freeze', 'Freezes time for 10 seconds', 50, 90, 1),
    ('Time Reverse', 'Reverses time by 5 minutes', 70, 85, 2),
    ('Time Acceleration', 'Speeds up time by 2x for 1 minute', 60, 80, 3);

-- Insert into Vehicle
INSERT INTO Vehicle (name, powerCapacity, engine, travelerID)
VALUES
    ('Time Machine', 500, 'Quantum Engine', 1),
    ('Chrono Cruiser', 400, 'Temporal Drive', 2),
    ('Eon Explorer', 600, 'Infinity Core', 3);

-- Insert into VehicleAbility
INSERT INTO VehicleAbility (name, description, powerConsumption, successProbability, vehicleID)
VALUES
    ('Time Jump', 'Jumps to a specific time period', 100, 95, 1),
    ('Time Shield', 'Creates a protective time barrier', 120, 90, 2),
    ('Time Warp', 'Distorts time in a localized area', 110, 85, 3);

SELECT * FROM VehicleAbility
WHERE vehicleID = 1;





