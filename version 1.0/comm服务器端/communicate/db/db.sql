-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.34-log - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 导出 communicate 的数据库结构
DROP DATABASE IF EXISTS `communicate`;
CREATE DATABASE IF NOT EXISTS `communicate` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `communicate`;

-- 导出  表 communicate.info 结构
DROP TABLE IF EXISTS `info`;
CREATE TABLE IF NOT EXISTS `info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientName` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '客户端名称',
  `fileName` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文件名称',
  `orgUrl` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '原始下载地址',
  `clientUrl` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '客户机下载地址',
  `online` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '是否在线',
  `clientIp` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '客户机的ip',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='信息';

-- 正在导出表  communicate.info 的数据：~0 rows (大约)
DELETE FROM `info`;
INSERT INTO `info` (`id`, `clientName`, `fileName`, `orgUrl`, `clientUrl`, `online`, `clientIp`) VALUES
	(5, 'W1', 'cifar-10-python.tar.gz', NULL, './datas/cifar-10-python.tar.gz', '1', 'http://127.0.0.1:8102/online'),
	(6, 'W1', 'cifar-10-python.tar.gz', NULL, './datas/cifar-10-python.tar.gz', '1', 'http://127.0.0.1:8102/online');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
