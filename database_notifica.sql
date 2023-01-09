/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80031
Source Host           : localhost:3306
Source Database       : database_notifica

Target Server Type    : MYSQL
Target Server Version : 80031
File Encoding         : 65001

Date: 2023-01-08 18:24:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `message`
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `mes_id` int NOT NULL AUTO_INCREMENT,
  `mes_datacreazione` datetime DEFAULT NULL,
  `mes_userCreator` varchar(45) DEFAULT NULL,
  `mes_tipomessaggio` int DEFAULT NULL,
  `mes_userDestinatario` varchar(45) DEFAULT NULL,
  `mes_dataScadenzaLettura` datetime DEFAULT NULL,
  `mes_userAlerting` varchar(45) DEFAULT NULL,
  `mes_tipoAlert` varchar(45) DEFAULT NULL,
  `mes_dataLettura` varchar(45) DEFAULT NULL,
  `mes_Stato` int DEFAULT NULL,
  `mes_idPadre` int DEFAULT NULL,
  `mes_Oggetto` varchar(45) DEFAULT NULL,
  `mes_Messaggio` varchar(45) DEFAULT NULL,
  `mes_sleep` datetime DEFAULT NULL,
  `mes_campiRisposta` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `mes_bottoni` text,
  PRIMARY KEY (`mes_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('1', '2023-01-07 09:59:10', 'Mattia', '0', 'Test', '2023-01-10 09:59:26', null, '1', null, '0', null, 'Testing', 'Ricorda Fatture', null, '[{\"obj\":\"testo\" ,\"label\":\"Testo\",\"id\":\"txt1\"},{\"obj\":\"combo\",\"valori\":[\"1\",\"5\",\"6\"] ,\"label\":\"Combo\",\"id\":\"combo1\"},{\"obj\":\"calendario\" ,\"label\":\"calendario\" ,\"id\":\"calendar\"},{\"obj\":\"timePicker\" ,\"label\":\"Scegli ora\" ,\"id\":\"timepicker\"},{\"obj\":\"bottone\" ,\"label\":\"Scegli ora\" ,\"id\":\"bottone\"},{\"obj\":\"checkboxlist\" ,\"label\":[\"Value A\",\"Value B\",\"Value C\"] ,\"id\":\"checkboxlist\"}]', '[{\"obj\":\"bottone\",\"label\":\"OK\",\"function\":\"self.close\",\"id\":\"bottonetmp1\"},{\"obj\":\"bottone\",\"label\":\"Registra\",\"function\":\"\",\"id\":\"bottonetmp2\"}]');
