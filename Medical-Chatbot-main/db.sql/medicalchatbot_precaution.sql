CREATE DATABASE  IF NOT EXISTS `medicalchatbot` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `medicalchatbot`;
WARNING: --delete-master-logs is deprecated and will be removed in a future version. Use --delete-source-logs instead.
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: medicalchatbot
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Position to start replication or point-in-time recovery from
--

-- CHANGE MASTER TO MASTER_LOG_FILE='LAPTOP-QBERAHK2-bin.000011', MASTER_LOG_POS=155;

--
-- Table structure for table `precaution`
--

DROP TABLE IF EXISTS `precaution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `precaution` (
  `disease` varchar(255) DEFAULT NULL,
  `precaution1` varchar(255) DEFAULT NULL,
  `precaution2` varchar(255) DEFAULT NULL,
  `precaution3` varchar(255) DEFAULT NULL,
  `precaution4` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `precaution`
--

LOCK TABLES `precaution` WRITE;
/*!40000 ALTER TABLE `precaution` DISABLE KEYS */;
REPLACE  IGNORE INTO `precaution` (`disease`, `precaution1`, `precaution2`, `precaution3`, `precaution4`) VALUES ('Malaria','Consult nearest hospital','Avoid oily food','Avoid non veg food','Keep mosquitos out'),('Allergy','Apply calamine','Cover area with bandage','','Use ice to compress itching'),('Hypothyroidism','Reduce stress','Exercise','Eat healthy','Get proper sleep'),('Psoriasis','Wash hands with warm soapy water','Stop bleeding using pressure','Consult doctor','Salt baths'),('Gerd','Avoid fatty spicy food','Avoid lying down after eating','Maintain healthy weight','Exercise'),('Chronic cholestasis','Cold baths','Anti itch medicine','Consult doctor','Eat healthy'),('Hepatitis a','Consult nearest hospital','Wash hands through','Avoid fatty spicy food','Medication'),('Osteoarthristis','Acetaminophen','Consult nearest hospital','Follow up','Salt baths'),('(Vertigo) Paroymsal  positional vertigo','Lie down','Avoid sudden change in body','Avoid abrupt head movment','Relax'),('Hypoglycemia','Lie down on side','Check in pulse','Drink sugary drinks','Consult doctor'),('Acne','Bath twice','Avoid fatty spicy food','Drink plenty of water','Avoid too many products'),('Diabetes ','Have balanced diet','Exercise','Consult doctor','Follow up'),('Impetigo','Soak affected area in warm water','Use antibiotics','Remove scabs with wet compressed cloth','Consult doctor'),('Hypertension ','Meditation','Salt baths','Reduce stress','Get proper sleep'),('Peptic ulcer diseae','Avoid fatty spicy food','Consume probiotic food','Eliminate milk','Limit alcohol'),('Dimorphic hemmorhoids(piles)','Avoid fatty spicy food','Consume witch hazel','Warm bath with epsom salt','Consume alovera juice'),('Common cold','Drink vitamin c rich drinks','Take vapour','Avoid cold food','Keep fever in check'),('Chicken pox','Use neem in bathing ','Consume neem leaves','Take vaccine','Avoid public places'),('Cervical spondylosis','Use heating pad or cold pack','Exercise','Take otc pain reliver','Consult doctor'),('Hyperthyroidism','Eat healthy','Massage','Use lemon balm','Take radioactive iodine treatment'),('Urinary tract infection','Drink plenty of water','Increase vitamin c intake','Drink cranberry juice','Take probiotics'),('Varicose veins','Lie down flat and raise the leg high','Use oinments','Use vein compression','Dont stand still for long'),('Paralysis (brain hemorrhage)','Massage','Eat healthy','Exercise','Consult doctor'),('Typhoid','Eat high calorie vegitables','Antiboitic therapy','Consult doctor','Medication'),('Hepatitis b','Consult nearest hospital','Vaccination','Eat healthy','Medication'),('Fungal infection','Bath twice','Use detol or neem in bathing water','Keep infected area dry','Use clean cloths'),('Hepatitis c','Consult nearest hospital','Vaccination','Eat healthy','Medication'),('Migraine','Meditation','Reduce stress','Use poloroid glasses in sun','Consult doctor'),('Bronchial asthma','Switch to loose cloothing','Take deep breaths','Get away from trigger','Seek help'),('Jaundice','Drink plenty of water','Consume milk thistle','Eat fruits and high fiberous food','Medication'),('Hepatitis e','Stop alcohol consumption','Rest','Consult doctor','Medication'),('Dengue','Drink papaya leaf juice','Avoid fatty spicy food','Keep mosquitos away','Keep hydrated'),('Hepatitis d','Consult doctor','Medication','Eat healthy','Follow up'),('Heart attack','Call ambulance','Chew or swallow asprin','Keep calm',''),('Pneumonia','Consult doctor','Medication','Rest','Follow up'),('Arthritis','Exercise','Use hot and cold therapy','Try acupuncture','Massage'),('Gastroenteritis','Stop eating solid food for while','Try taking small sips of water','Rest','Ease back into eating'),('Tuberculosis','Cover mouth','Consult doctor','Medication','Rest');
/*!40000 ALTER TABLE `precaution` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-27 22:18:12
