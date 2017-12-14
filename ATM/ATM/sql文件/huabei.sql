/*
Navicat MySQL Data Transfer

Source Server         : 192.168.1.111
Source Server Version : 50604
Source Host           : 192.168.1.111:3306
Source Database       : huabei

Target Server Type    : MYSQL
Target Server Version : 50604
File Encoding         : 65001

Date: 2017-07-04 18:22:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for hb_borrow
-- ----------------------------
DROP TABLE IF EXISTS `hb_borrow`;
CREATE TABLE `hb_borrow` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `borrow_done` varchar(255) DEFAULT NULL,
  `huabei_limit` decimal(65,2) DEFAULT NULL,
  `huabei_residue_limit` decimal(65,2) DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `isrepayment` int(1) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hb_borrow
-- ----------------------------
INSERT INTO `hb_borrow` VALUES ('1', 'lisi', '杀人', '2000.00', null, '2017-06-28', '1');
INSERT INTO `hb_borrow` VALUES ('2', 'wangqiyuan', '200', '3000.00', '3000.00', '2017-07-04', '1');
INSERT INTO `hb_borrow` VALUES ('10', '123', '', '3000.00', '3000.00', '0000-00-00', '0');
INSERT INTO `hb_borrow` VALUES ('13', 'fdas', '', '3000.00', '3000.00', '0000-00-00', '0');

-- ----------------------------
-- Table structure for hb_borrow_info
-- ----------------------------
DROP TABLE IF EXISTS `hb_borrow_info`;
CREATE TABLE `hb_borrow_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `borrow_info` varchar(255) DEFAULT NULL,
  `borrow_num` decimal(11,0) DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hb_borrow_info
-- ----------------------------
INSERT INTO `hb_borrow_info` VALUES ('2', 'wangqiyuan', '吃饭', null, '2017-07-04');
INSERT INTO `hb_borrow_info` VALUES ('3', 'wangqiyuan', '吃饭', '2000', '2017-07-04');
INSERT INTO `hb_borrow_info` VALUES ('4', 'wangqiyuan', '200', '200', '2017-07-04');

-- ----------------------------
-- Table structure for hb_repayment_info
-- ----------------------------
DROP TABLE IF EXISTS `hb_repayment_info`;
CREATE TABLE `hb_repayment_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `repayment_num` decimal(10,0) DEFAULT NULL,
  `repayment_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hb_repayment_info
-- ----------------------------
INSERT INTO `hb_repayment_info` VALUES ('1', 'wangqiyuan', '1000', '2017-07-04');
INSERT INTO `hb_repayment_info` VALUES ('2', 'wangqiyuan', '200', '2017-07-04');
