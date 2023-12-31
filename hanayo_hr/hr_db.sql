DROP DATABASE IF EXISTS hanayo_hr_db;
-- -------------------------
--               建库
-- -------------------------
CREATE DATABASE hanayo_hr_db default character set utf8mb4;
USE hanayo_hr_db;

-- ----------------------
-- 建一个data表，存储爬取的职位信息
-- ----------------------
DROP TABLE IF EXISTS `tb_data`;
CREATE TABLE `tb_data`(
	`data_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据ID',
	`data_post` VARCHAR(255) NOT NULL COMMENT '职位',
	`data_company` VARCHAR(255) NOT NULL COMMENT '公司名称',
	`data_address` VARCHAR(50) NOT NULL COMMENT '公司地址',
	`data_salary_min` int(11) NOT NULL COMMENT '薪资min/月',
    `data_salary_max` int(11) NOT NULL COMMENT '薪资max/月' ,
    `data_date` DATE NOT NULL COMMENT '发布日期',
    `data_edu` VARCHAR(50) NOT NULL COMMENT '学历',
    `data_exp` VARCHAR(50) NOT NULL COMMENT '经验',
    `data_content` TEXT NOT NULL COMMENT '招聘详情',
    PRIMARY KEY(`data_id`)
)engine=innodb auto_increment=1 comment '职位数据表';



-- ------------------------
-- 建一个city表，存储每一地区的的编码对应的地区
-- ------------------------
DROP TABLE IF EXISTS `tb_city`;
CREATE TABLE `tb_city`(
	`city_id` int(11) NOT NULL COMMENT '城市ID',
	`city_name` varchar(30) NOT NULL COMMENT '城市',
    PRIMARY KEY(`city_id`)
)ENGINE=InnoDB comment '城市代码表';


INSERT INTO `tb_city` VALUES ('530', '北京'),('538', '上海');

-- ----------------------
-- 建一个keys表，存储已经爬取过的关键词
-- ----------------------
DROP TABLE IF EXISTS `tb_keys`;
CREATE TABLE `tb_keys`(
	`keys_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '关键词ID',
	`keys_name` varchar(30) NOT NULL COMMENT '关键词名称',
	`keys_count` int(11) NOT NULL COMMENT '点击量',
    PRIMARY KEY(`keys_id`)
)ENGINE=InnoDB auto_increment=1 comment '关键词表';

INSERT INTO `tb_keys` (keys_name, keys_count) VALUES ('python', 2),('java', 1);
