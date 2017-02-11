-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	5.6.34

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
-- Table structure for table `Business_detail`
--

DROP TABLE IF EXISTS `Business_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Business_detail` (
  `id` int(11) NOT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `industry` varchar(45) DEFAULT NULL,
  `street address` varchar(45) DEFAULT NULL,
  `Businesses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Business detail_Businesses1_idx` (`Businesses_id`),
  CONSTRAINT `fk_Business detail_Businesses1` FOREIGN KEY (`Businesses_id`) REFERENCES `Businesses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Business_detail`
--

LOCK TABLES `Business_detail` WRITE;
/*!40000 ALTER TABLE `Business_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `Business_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Businesses`
--

DROP TABLE IF EXISTS `Businesses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Businesses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `owner` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Businesses`
--

LOCK TABLES `Businesses` WRITE;
/*!40000 ALTER TABLE `Businesses` DISABLE KEYS */;
INSERT INTO `Businesses` VALUES (1,'2017-02-09 14:28:02','2017-02-09 14:28:02','Safeway','various'),(3,'2017-02-09 15:05:45','2017-02-09 15:05:45','Tullys','Patrick Dempsey'),(4,'2017-02-09 15:05:45','2017-02-09 15:05:45','Starbucks','Howard Schultz'),(5,'2017-02-09 15:05:45','2017-02-09 15:05:45','Coding Dojo','Michael Choi'),(6,'2017-02-09 15:05:45','2017-02-09 15:05:45','Joes Garage','Joe'),(7,'2017-02-09 15:05:45','2017-02-09 15:05:45','US Bank','Who knows');
/*!40000 ALTER TABLE `Businesses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Businesses_has_Cities`
--

DROP TABLE IF EXISTS `Businesses_has_Cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Businesses_has_Cities` (
  `id` int(11) NOT NULL,
  `Cities_id` int(11) NOT NULL,
  `Businesses_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Businesses_has_Cities_Cities1_idx` (`Cities_id`),
  KEY `fk_Businesses_has_Cities_Businesses1_idx` (`Businesses_id`),
  CONSTRAINT `fk_Businesses_has_Cities_Businesses1` FOREIGN KEY (`Businesses_id`) REFERENCES `Businesses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Businesses_has_Cities_Cities1` FOREIGN KEY (`Cities_id`) REFERENCES `Cities` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Businesses_has_Cities`
--

LOCK TABLES `Businesses_has_Cities` WRITE;
/*!40000 ALTER TABLE `Businesses_has_Cities` DISABLE KEYS */;
/*!40000 ALTER TABLE `Businesses_has_Cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cities`
--

DROP TABLE IF EXISTS `Cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `States_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Cities_States_idx` (`States_id`),
  CONSTRAINT `fk_Cities_States` FOREIGN KEY (`States_id`) REFERENCES `States` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cities`
--

LOCK TABLES `Cities` WRITE;
/*!40000 ALTER TABLE `Cities` DISABLE KEYS */;
INSERT INTO `Cities` VALUES (1,'2017-02-09 14:27:59','2017-02-09 14:27:59','Seattle',1),(3,'2017-02-09 14:45:58','2017-02-09 14:45:58','Moses Lake',1),(4,'2017-02-09 14:45:58','2017-02-09 14:45:58','Darrington',1),(5,'2017-02-09 14:45:58','2017-02-09 14:45:58','Everett',1),(6,'2017-02-09 14:45:58','2017-02-09 14:45:58','Tacoma',1);
/*!40000 ALTER TABLE `Cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `States`
--

DROP TABLE IF EXISTS `States`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `States` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `abbreviation` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `States`
--

LOCK TABLES `States` WRITE;
/*!40000 ALTER TABLE `States` DISABLE KEYS */;
INSERT INTO `States` VALUES (1,'2017-02-09 14:27:56','2017-02-09 14:27:56','Washington','WA'),(3,'2017-02-09 14:45:58','2017-02-09 14:45:58','Idaho','ID'),(4,'2017-02-09 14:45:58','2017-02-09 14:45:58','Oregon','OR'),(5,'2017-02-09 14:45:58','2017-02-09 14:45:58','California','CA'),(6,'2017-02-09 14:45:58','2017-02-09 14:45:58','Alaska','AK'),(7,'2017-02-09 14:45:58','2017-02-09 14:45:58','Delaware','DE');
/*!40000 ALTER TABLE `States` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-10  8:32:29
