-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: TimeTravelingSchema
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Companion`
--

DROP TABLE IF EXISTS `Companion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Companion` (
  `companionID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT 'Unknown',
  `age` int unsigned NOT NULL DEFAULT '18',
  `originalLocation` varchar(100) DEFAULT 'Unknown',
  `currentTimePeriod` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `travelerID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`companionID`),
  KEY `travelerID` (`travelerID`),
  KEY `name_index` (`name`),
  CONSTRAINT `companion_ibfk_1` FOREIGN KEY (`travelerID`) REFERENCES `Traveler` (`travelerID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Companion`
--

LOCK TABLES `Companion` WRITE;
/*!40000 ALTER TABLE `Companion` DISABLE KEYS */;
INSERT INTO `Companion` VALUES (1,'Jane Smith',28,'Mars','2023-10-01 12:00:00',1),(2,'Emily Davis',22,'Jupiter','2023-10-02 14:00:00',2),(3,'Michael Lee',35,'Saturn','2023-10-03 16:00:00',3),(4,'Daniel Underhill',35,'London','2025-05-06 23:13:49',3),(5,'Daniel McPeterson',74,'New York','2025-05-06 23:27:25',1),(8,'Test4',50,'New Orleans','2025-05-23 16:52:25',6);
/*!40000 ALTER TABLE `Companion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tool`
--

DROP TABLE IF EXISTS `Tool`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tool` (
  `toolID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT 'Unknown',
  `powerCapacity` int NOT NULL DEFAULT '100',
  `travelerID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`toolID`),
  KEY `travelerID` (`travelerID`),
  CONSTRAINT `tool_ibfk_1` FOREIGN KEY (`travelerID`) REFERENCES `Traveler` (`travelerID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tool`
--

LOCK TABLES `Tool` WRITE;
/*!40000 ALTER TABLE `Tool` DISABLE KEYS */;
INSERT INTO `Tool` VALUES (1,'Time Watch',200,1),(2,'Quantum Compass',150,2),(3,'Temporal Scanner',300,3),(4,'Hot Dog',1000,5),(6,'Screwdriver',0,7);
/*!40000 ALTER TABLE `Tool` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ToolAbility`
--

DROP TABLE IF EXISTS `ToolAbility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ToolAbility` (
  `toolAbilityID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT 'Unknown',
  `description` varchar(750) NOT NULL DEFAULT 'Unknown',
  `powerConsumption` int NOT NULL DEFAULT '10',
  `successProbability` int NOT NULL DEFAULT '50',
  `toolID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`toolAbilityID`),
  KEY `toolID` (`toolID`),
  CONSTRAINT `toolability_ibfk_1` FOREIGN KEY (`toolID`) REFERENCES `Tool` (`toolID`),
  CONSTRAINT `restrict_toolAbilityProbability` CHECK ((`successProbability` between 1 and 100))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ToolAbility`
--

LOCK TABLES `ToolAbility` WRITE;
/*!40000 ALTER TABLE `ToolAbility` DISABLE KEYS */;
INSERT INTO `ToolAbility` VALUES (1,'Time Freeze','Freezes time for 10 seconds',50,90,1),(2,'Time Reverse','Reverses time by 5 minutes',70,85,2),(3,'Time Acceleration','Speeds up time by 2x for 1 minute',60,80,3);
/*!40000 ALTER TABLE `ToolAbility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Traveler`
--

DROP TABLE IF EXISTS `Traveler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Traveler` (
  `travelerID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT 'Unknown',
  `age` int unsigned NOT NULL DEFAULT '18',
  `birthLocation` varchar(100) NOT NULL DEFAULT 'Unknown',
  `currentTimePeriod` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`travelerID`),
  KEY `name_index` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Traveler`
--

LOCK TABLES `Traveler` WRITE;
/*!40000 ALTER TABLE `Traveler` DISABLE KEYS */;
INSERT INTO `Traveler` VALUES (1,'John Doe',30,'Earth','2023-10-01 12:00:00'),(2,'Alice Johnson',25,'Venus','2023-10-02 14:00:00'),(3,'Bob Brown',40,'Mars','2023-10-03 16:00:00'),(4,'Daniel Roberts',47,'Orlando','2025-05-06 23:46:38'),(5,'sample text 2',57,'planet 2','2025-05-07 00:10:08'),(6,'Joshua Roberts',32,'Salt Lake City','2025-05-07 16:55:18'),(7,'Dan',25,'LA','2025-05-07 17:58:55');
/*!40000 ALTER TABLE `Traveler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Trip`
--

DROP TABLE IF EXISTS `Trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Trip` (
  `tripID` int unsigned NOT NULL AUTO_INCREMENT,
  `location` varchar(100) NOT NULL DEFAULT 'Unknown',
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `imageFile` varchar(1000) NOT NULL DEFAULT 'Unknown',
  `travelerID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`tripID`),
  KEY `travelerID` (`travelerID`),
  CONSTRAINT `trip_ibfk_1` FOREIGN KEY (`travelerID`) REFERENCES `Traveler` (`travelerID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trip`
--

LOCK TABLES `Trip` WRITE;
/*!40000 ALTER TABLE `Trip` DISABLE KEYS */;
INSERT INTO `Trip` VALUES (1,'Ancient Rome','2023-10-01 12:00:00','rome.jpg',1),(2,'Medieval England','2023-10-02 14:00:00','england.jpg',2),(3,'Future Mars','2023-10-03 16:00:00','mars.jpg',3),(4,'Rome','2025-05-12 17:06:57','realImage.png',7),(5,'Super Earth','2025-05-20 11:36:10','superEarth.png',3),(9,'test2','2025-05-23 14:24:10','realphoto10',6);
/*!40000 ALTER TABLE `Trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_master_records`
--

DROP TABLE IF EXISTS `v_master_records`;
/*!50001 DROP VIEW IF EXISTS `v_master_records`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_master_records` AS SELECT 
 1 AS `tripID`,
 1 AS `location`,
 1 AS `trip_date`,
 1 AS `imageFile`,
 1 AS `TravelerID`,
 1 AS `traveler_name`,
 1 AS `traveler_age`,
 1 AS `traveler_origin`,
 1 AS `traveler_time_period`,
 1 AS `companion_id`,
 1 AS `companionID`,
 1 AS `companion_name`,
 1 AS `companion_age`,
 1 AS `companion_origin`,
 1 AS `companion_time_period`,
 1 AS `tool_id`,
 1 AS `tool_name`,
 1 AS `tool_power_capacity`,
 1 AS `tool_ability_id`,
 1 AS `tool_ability_name`,
 1 AS `tool_ability_description`,
 1 AS `tool_ability_power_consumption`,
 1 AS `tool_ability_success`,
 1 AS `vehicle_id`,
 1 AS `vehicle_name`,
 1 AS `vehicle_power_capacity`,
 1 AS `vehicle_engine`,
 1 AS `vehicle_ability_id`,
 1 AS `vehicle_ability_name`,
 1 AS `vehicle_ability_description`,
 1 AS `vehicle_ability_power_consumption`,
 1 AS `vehicle_ability_success`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Vehicle`
--

DROP TABLE IF EXISTS `Vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Vehicle` (
  `vehicleID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT 'Unknown',
  `powerCapacity` int NOT NULL DEFAULT '100',
  `engine` varchar(100) NOT NULL DEFAULT 'Unknown',
  `travelerID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`vehicleID`),
  KEY `travelerID` (`travelerID`),
  CONSTRAINT `vehicle_ibfk_1` FOREIGN KEY (`travelerID`) REFERENCES `Traveler` (`travelerID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vehicle`
--

LOCK TABLES `Vehicle` WRITE;
/*!40000 ALTER TABLE `Vehicle` DISABLE KEYS */;
INSERT INTO `Vehicle` VALUES (1,'Time Machine',500,'Quantum Engine',1),(2,'Chrono Cruiser',400,'Temporal Drive',2),(3,'Eon Explorer',600,'Infinity Core',3),(4,'DMC DeLorean',130,'PRV ZMJ-159',5),(6,'LeCar',25,'LeEngine',6);
/*!40000 ALTER TABLE `Vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VehicleAbility`
--

DROP TABLE IF EXISTS `VehicleAbility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VehicleAbility` (
  `vehicleAbilityID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT 'Unknown',
  `description` varchar(750) NOT NULL DEFAULT 'Unknown',
  `powerConsumption` int NOT NULL DEFAULT '10',
  `successProbability` int NOT NULL DEFAULT '50',
  `vehicleID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`vehicleAbilityID`),
  KEY `vehicleID` (`vehicleID`),
  CONSTRAINT `vehicleability_ibfk_1` FOREIGN KEY (`vehicleID`) REFERENCES `Vehicle` (`vehicleID`),
  CONSTRAINT `restrict_vehicleAbilityProbability` CHECK ((`successProbability` between 1 and 100))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VehicleAbility`
--

LOCK TABLES `VehicleAbility` WRITE;
/*!40000 ALTER TABLE `VehicleAbility` DISABLE KEYS */;
INSERT INTO `VehicleAbility` VALUES (1,'Time Jump','Jumps to a specific time period',100,95,1),(2,'Time Shield','Creates a protective time barrier',120,90,2),(3,'Time Warp','Distorts time in a localized area',110,85,3);
/*!40000 ALTER TABLE `VehicleAbility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `v_master_records`
--

/*!50001 DROP VIEW IF EXISTS `v_master_records`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_master_records` AS select distinct `trip`.`tripID` AS `tripID`,`trip`.`location` AS `location`,`trip`.`date` AS `trip_date`,`trip`.`imageFile` AS `imageFile`,`traveler`.`travelerID` AS `TravelerID`,`traveler`.`name` AS `traveler_name`,`traveler`.`age` AS `traveler_age`,`traveler`.`birthLocation` AS `traveler_origin`,`traveler`.`currentTimePeriod` AS `traveler_time_period`,`companion`.`companionID` AS `companion_id`,`companion`.`companionID` AS `companionID`,`companion`.`name` AS `companion_name`,`companion`.`age` AS `companion_age`,`companion`.`originalLocation` AS `companion_origin`,`companion`.`currentTimePeriod` AS `companion_time_period`,`tool`.`toolID` AS `tool_id`,`tool`.`name` AS `tool_name`,`tool`.`powerCapacity` AS `tool_power_capacity`,`toolability`.`toolAbilityID` AS `tool_ability_id`,`toolability`.`name` AS `tool_ability_name`,`toolability`.`description` AS `tool_ability_description`,`toolability`.`powerConsumption` AS `tool_ability_power_consumption`,`toolability`.`successProbability` AS `tool_ability_success`,`vehicle`.`vehicleID` AS `vehicle_id`,`vehicle`.`name` AS `vehicle_name`,`vehicle`.`powerCapacity` AS `vehicle_power_capacity`,`vehicle`.`engine` AS `vehicle_engine`,`vehicleability`.`vehicleAbilityID` AS `vehicle_ability_id`,`vehicleability`.`name` AS `vehicle_ability_name`,`vehicleability`.`description` AS `vehicle_ability_description`,`vehicleability`.`powerConsumption` AS `vehicle_ability_power_consumption`,`vehicleability`.`successProbability` AS `vehicle_ability_success` from ((((((`trip` left join `traveler` on((`traveler`.`travelerID` = `trip`.`travelerID`))) left join `companion` on((`companion`.`travelerID` = `traveler`.`travelerID`))) left join `tool` on((`tool`.`travelerID` = `traveler`.`travelerID`))) left join `toolability` on((`tool`.`toolID` = `toolability`.`toolID`))) left join `vehicle` on((`vehicle`.`travelerID` = `traveler`.`travelerID`))) left join `vehicleability` on((`vehicle`.`vehicleID` = `vehicleability`.`vehicleID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-23 17:28:28
