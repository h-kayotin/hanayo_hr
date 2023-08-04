DROP DATABASE IF EXISTS u1;
-- -------------------------
--               建库
-- -------------------------
CREATE DATABASE u1;
USE u1;

-- ----------------------
-- 建一个data表，存储爬取的职位信息
-- ----------------------
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data`(
	`data_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据ID',
	`post` VARCHAR(30) NOT NULL COMMENT '职位',
	`company` VARCHAR(255) NOT NULL COMMENT '公司名称',
	`address` VARCHAR(50) NOT NULL COMMENT '公司地址',
	`salary_min` int(11) NOT NULL COMMENT '薪资min/月',
    `salary_max` int(11) NOT NULL COMMENT '薪资max/月' ,
    `dateT` VARCHAR(50) NOT NULL COMMENT '发布时间',
    `edu` VARCHAR(50) NOT NULL COMMENT '学历',
    `exper` VARCHAR(50) NOT NULL COMMENT '经验',
    `content` TEXT NOT NULL COMMENT '招聘详情',
    PRIMARY KEY(`data_id`)
)ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;



-- ------------------------
-- 建一个city表，存储每一地区的的编码对应的地区
-- ------------------------
DROP TABLE IF EXISTS `city`;
CREATE TABLE `city`(
	`city_id` varchar(11) NOT NULL COMMENT '城市ID',
	`city_name` varchar(30) NOT NULL COMMENT '城市',
    PRIMARY KEY(`city_id`)
)ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;



INSERT INTO `city` VALUES ('000000', '全国'),('010000', '北京'),('020000', '上海'),('030000', '广东'),('070000', '江苏'),('080000','浙江'),('090000','四川'),
                        ('100000','海南'),('110000','福建'),('120000','山东'),('130000','江西'),('140000','广西'),('150000','安徽'),('160000','河北省'),
                        ('170000','河南'),('180000','湖北'),('190000','湖南'),('200000','陕西'),('210000','山西'),('220000','黑龙江'),('230000','辽宁'),
                        ('240000','吉林'),('250000','云南'),('260000','贵州'),('270000','甘肃'),('280000','内蒙古'),('290000','宁夏'),('300000','西藏'),
                        ('310000','新疆'),('320000','青海'),
                        ('330000','香港'),
                        ('340000','澳门'),
                        ('350000','台湾');
            
