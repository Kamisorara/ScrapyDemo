/*
 Navicat Premium Data Transfer

 Source Server         : Docker本地数据库
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : scrapyTest

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 01/10/2022 23:09:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stocks
-- ----------------------------
DROP TABLE IF EXISTS `stocks`;
CREATE TABLE `stocks`  (
  `code` bigint NOT NULL COMMENT '股票代码',
  `abbreviation` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票简称',
  `marketValue` int NULL DEFAULT NULL COMMENT '流通市值(万元)',
  `totalValue` int NULL DEFAULT NULL COMMENT '总市值(万元)',
  `LIQUI` int NULL DEFAULT NULL COMMENT '流通股本(万元)',
  `generalCapital` int NULL DEFAULT NULL COMMENT '总股本(万元)',
  PRIMARY KEY (`code`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
