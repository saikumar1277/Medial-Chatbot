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

-- CHANGE MASTER TO MASTER_LOG_FILE='LAPTOP-QBERAHK2-bin.000012', MASTER_LOG_POS=155;

--
-- Table structure for table `description`
--

DROP TABLE IF EXISTS `description`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `description` (
  `disease` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `description`
--

LOCK TABLES `description` WRITE;
/*!40000 ALTER TABLE `description` DISABLE KEYS */;
REPLACE  IGNORE INTO `description` (`disease`, `description`) VALUES ('Malaria','An infectious disease caused by protozoan parasites from the plasmodium family that can be transmitted by the bite of the anopheles mosquito or by a contaminated needle or transfusion.'),('Allergy','An allergy is an immune system response to a foreign substance that\'s not typically harmful to your body.'),('Hypothyroidism','Hypothyroidism, also called underactive thyroid or low thyroid, is a disorder of the endocrine system in which the thyroid gland does not produce enough thyroid hormone.'),('Psoriasis','Psoriasis is a common skin disorder that forms thick, red, bumpy patches covered with silvery scales.'),('Gerd','Gastroesophageal reflux disease, or gerd, is a digestive disorder that affects the lower esophageal sphincter (les), the ring of muscle between the esophagus and stomach.'),('Chronic cholestasis','Chronic cholestatic diseases, whether occurring in infancy, childhood or adulthood, are characterized by defective bile acid transport from the liver to the intestine, which is caused by primary damage to the biliary epithelium in most cases.'),('Hepatitis a','Hepatitis a is a highly contagious liver infection caused by the hepatitis a virus.'),('Osteoarthristis','Osteoarthritis is the most common form of arthritis, affecting millions of people worldwide.'),('(Vertigo) Paroymsal  positional vertigo','Benign paroxysmal positional vertigo (bppv) is one of the most common causes of vertigo â€” the sudden sensation that you\'re spinning or that the inside of your head is spinning.'),('Hypoglycemia','Hypoglycemia is a condition in which your blood sugar (glucose) level is lower than normal.'),('Acne','Acne vulgaris is the formation of comedones, papules, pustules, nodules, and/or cysts as a result of obstruction and inflammation of pilosebaceous units (hair follicles and their accompanying sebaceous gland).'),('Diabetes','Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high.'),('Impetigo','Impetigo (im-puh-tie-go) is a common and highly contagious skin infection that mainly affects infants and children.'),('Hypertension','Hypertension (htn or ht), also known as high blood pressure (hbp), is a long-term medical condition in which the blood pressure in the arteries is persistently elevated.'),('Peptic ulcer diseae','Peptic ulcer disease (pud) is a break in the inner lining of the stomach, the first part of the small intestine, or sometimes the lower esophagus.'),('Dimorphic hemorrhoids(piles)','Hemorrhoids, also spelled haemorrhoids, are vascular structures in the anal canal.'),('Common cold','The common cold is a viral infection of your nose and throat (upper respiratory tract).'),('Chicken pox','Chickenpox is a highly contagious disease caused by the varicella-zoster virus (vzv).'),('Cervical spondylosis','Cervical spondylosis is a general term for age-related wear and tear affecting the spinal disks in your neck.'),('Hyperthyroidism','Hyperthyroidism (overactive thyroid) occurs when your thyroid gland produces too much of the hormone thyroxine.'),('Urinary tract infection','Urinary tract infection: an infection of the kidney, ureter, bladder, or urethra.'),('Varicose veins','A vein that has enlarged and twisted, often appearing as a bulging, blue blood vessel that is clearly visible through the skin.'),('Paralysis (brain hemorrhage)','Intracerebral hemorrhage (ich) is when blood suddenly bursts into brain tissue, causing damage to your brain.'),('Typhoid','An acute illness characterized by fever caused by infection with the bacterium salmonella typhi.'),('Hepatitis b','Hepatitis b is an infection of your liver.'),('Fungal infection','In humans, fungal infections occur when an invading fungus takes over an area of the body and is too much for the immune system to handle.'),('Hepatitis c','Inflammation of the liver due to the hepatitis c virus (hcv), which is usually spread via blood transfusion (rare), hemodialysis, and needle sticks.'),('Migraine','A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head.'),('Bronchial asthma','Bronchial asthma is a medical condition which causes the airway path of the lungs to swell and narrow.'),('Jaundice','Yellow staining of the skin and sclerae (the whites of the eyes) by abnormally high blood levels of the bile pigment bilirubin.'),('Hepatitis e','A rare form of liver inflammation caused by infection with the hepatitis e virus (hev).'),('Dengue','An acute infectious disease caused by a flavivirus (species dengue virus of the genus flavivirus), transmitted by aedes mosquitoes, and characterized by headache, severe joint pain, and a rash.'),('Hepatitis d','Hepatitis d, also known as the hepatitis delta virus, is an infection that causes the liver to become inflamed.'),('Heart attack','The death of heart muscle due to the loss of blood supply.'),('Pneumonia','Pneumonia is an infection in one or both lungs.'),('Arthritis','Arthritis is the swelling and tenderness of one or more of your joints.'),('Gastroenteritis','Gastroenteritis is an inflammation of the digestive tract, particularly the stomach, and large and small intestines.'),('Tuberculosis','Tuberculosis (tb) is an infectious disease usually caused by mycobacterium tuberculosis (mtb) bacteria.');
/*!40000 ALTER TABLE `description` ENABLE KEYS */;
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
