-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `subjectcode` varchar(8) DEFAULT NULL,
  `name` varchar(25) DEFAULT NULL,
  `author` varchar(25) DEFAULT NULL,
  `subject` varchar(15) DEFAULT NULL,
  `class` varchar(5) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `status` char(1) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'22EC001','Basic Electronics','N.N Bhargava','BEE','1styr',600,'Y'),(2,'22EC001','Basic Electronics','N.N Bhargava','BEE','1styr',600,'Y'),(3,'22EC001','Basic Electronics','Muthusubramania','BEE','1styr',650,'Y'),(4,'22EC001','Basic Electronics','Muthusubramania','BEE','1styr',650,'Y'),(5,'22EC001','Basic Electronics','Kothari','BEE','1styr',400,'Y'),(6,'22EC001','Basic Electronics','Kothari','BEE','1styr',400,'Y'),(7,'CS181','Pro Git','Scott chacon','SCM','1styr',670,'Y'),(8,'CS181','Pro Git','Scott chacon','SCM','1styr',670,'Y'),(9,'CS181','Learn Git','Jameson Garner','SCM','1styr',250,'N'),(10,'CS181','Learn Git','Jameson Garner','SCM','1styr',250,'Y'),(11,'22AS015','Engineering Physics','HK Malik','MCP','1styr',980,'N'),(12,'22AS015','Engineering Physics','HK Malik','MCP','1styr',980,'N'),(13,'22AS015','Engineering Physics','HK Malik','MCP','1styr',980,'Y'),(14,'22AS015','Engineering Physics','Chitkara Publications','MCP','1styr',980,'Y'),(15,'22AS015','Engineering Physics','Chitkara Publications','MCP','1styr',980,'Y'),(16,'22AS015','Engineering Physics','Chitkara Publications','MCP','1styr',980,'Y'),(17,'22AS015','Engineering Physics','Chitkara Publications','MCP','1styr',980,'Y'),(18,'22AS015','Engineering Physics','Chitkara Publications','MCP','1styr',980,'N');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `createstdacc`
--

DROP TABLE IF EXISTS `createstdacc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `createstdacc` (
  `rollno` varchar(10) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `emailaddress` varchar(50) DEFAULT NULL,
  `grp` varchar(3) DEFAULT NULL,
  `branch` varchar(5) DEFAULT NULL,
  `password` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`rollno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `createstdacc`
--

LOCK TABLES `createstdacc` WRITE;
/*!40000 ALTER TABLE `createstdacc` DISABLE KEYS */;
INSERT INTO `createstdacc` VALUES ('2210991642','Harshita','harshita19062004@gmail.com','7-B','CSE','demopass'),('2210991643','Harshita','harshita17@gmail.com','7-B','CSE','pass1234'),('2210991644','Harshita','harshita90@gmail.com','7-B','CSE','rtd6709t'),('2210991645','Hitaishi','hitaishi1666@gmail.com','7-B','CSE','31Riwub&'),('2210991646','Akhil Goyal','goyalakhil06022004@gmail.com','7-B','CSE','s+!0|MsX');
/*!40000 ALTER TABLE `createstdacc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `createuseracc`
--

DROP TABLE IF EXISTS `createuseracc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `createuseracc` (
  `username` varchar(15) NOT NULL,
  `phoneno` varchar(10) DEFAULT NULL,
  `password` varchar(8) DEFAULT NULL,
  `emailaddress` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `createuseracc`
--

LOCK TABLES `createuseracc` WRITE;
/*!40000 ALTER TABLE `createuseracc` DISABLE KEYS */;
INSERT INTO `createuseracc` VALUES ('_aa_stha','9814203170','demopass','aastha707@gmail.com'),('apeksha_12','6578023497','19062004','apkshu980@gmail.com'),('hrshita_90','9465731174','#4$ghijk','harshita19062004@gmail.com');
/*!40000 ALTER TABLE `createuseracc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fine_charges`
--

DROP TABLE IF EXISTS `fine_charges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fine_charges` (
  `S_No` int NOT NULL AUTO_INCREMENT,
  `fine_per_day` int DEFAULT NULL,
  `no_of_days` int DEFAULT NULL,
  `fine` int DEFAULT NULL,
  PRIMARY KEY (`S_No`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fine_charges`
--

LOCK TABLES `fine_charges` WRITE;
/*!40000 ALTER TABLE `fine_charges` DISABLE KEYS */;
INSERT INTO `fine_charges` VALUES (1,5,4,20),(2,5,2,10),(3,5,0,0),(4,5,2,10),(5,5,2,10),(6,5,1,5),(7,5,13,65),(8,5,0,0),(9,5,1,5),(10,5,2,10),(11,5,30,150);
/*!40000 ALTER TABLE `fine_charges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `rollno` varchar(10) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `phoneno` char(10) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`rollno`),
  UNIQUE KEY `phoneno` (`phoneno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('2210991132','Rahul','9465722274','9'),('2210991176','Ankita','975682340','9'),('2210991412','Riya','9465731174','11'),('2210991582','Priya','9743520876','10'),('2210991642','Harshita','9823408565','8'),('2210991666','Hitaishi','9823408455','1styr'),('2210991672','Aakshi','9876598324','10'),('2210992001','Keshav Kathuria','6754398715','1styr');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentcard`
--

DROP TABLE IF EXISTS `studentcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studentcard` (
  `S_No` int NOT NULL AUTO_INCREMENT,
  `Rollno` varchar(10) DEFAULT NULL,
  `Book_Id` varchar(25) DEFAULT NULL,
  `Issued_data` datetime DEFAULT NULL,
  `Return_date` datetime DEFAULT NULL,
  `actual_returning_date` datetime DEFAULT NULL,
  PRIMARY KEY (`S_No`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentcard`
--

LOCK TABLES `studentcard` WRITE;
/*!40000 ALTER TABLE `studentcard` DISABLE KEYS */;
INSERT INTO `studentcard` VALUES (1,'2210991130','30254','2022-12-05 11:23:42','2023-02-13 14:46:00','2023-01-30 15:34:21'),(2,'2210991280','32456','2022-12-05 11:40:50','2022-12-17 11:40:50','2022-12-19 15:37:15'),(3,'2210991656','48763','2022-12-05 12:19:06','2022-12-12 12:19:06','2022-12-12 09:12:15'),(4,'2210996573','23457','2022-12-05 12:19:37','2022-12-15 12:19:37','2022-12-07 16:12:15'),(5,'2210991382','2345','2022-12-05 12:56:37','2022-12-11 12:56:37','2022-12-13 18:25:56'),(8,'2210991412','KR198','2022-12-05 12:59:45','2022-12-12 13:02:16','2023-02-06 14:48:38'),(9,'2210991642','KR196','2022-12-05 13:02:16','2022-12-12 13:02:16','2023-02-06 14:38:59'),(10,'2210991130','KR157','2022-12-05 13:03:33','2022-12-20 13:03:33','2022-12-20 10:37:48'),(11,'2210991072','KR069','2022-12-07 23:09:28','2022-12-20 23:09:28','2023-01-30 15:39:00'),(12,'2210991583','KR017','2022-12-16 11:17:44','2022-12-23 11:17:44','2023-01-30 15:39:40'),(13,'2210992850','KR890','2022-12-17 11:53:05','2022-12-29 11:53:05','2023-01-30 15:43:22'),(14,'2210991165','9','2023-02-06 20:20:19','2023-02-13 20:20:19',NULL),(15,'2210991195','12','2023-02-06 20:21:09','2023-02-13 20:21:09',NULL),(16,'2210991412','18','2023-02-16 14:43:16','2023-02-17 14:43:16',NULL);
/*!40000 ALTER TABLE `studentcard` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-26 16:55:16
