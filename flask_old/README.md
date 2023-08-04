# 可视化职业分析系统安装使用说明

## 项目简介

本项目使用的编程语言是`python3`，数据库用的是`MySQL`, 主要用到的库是`Flask`和`requests`，使用`HighCharts` + `Bootstrap` 来构建前端页面，主要爬取数据对象是`51job.com`，通过用户输入条件，实时爬取网站内容，并通过`HighCharts`构建可视化页面。

## 环境要求

- Python 3.6+
- MySQL 5.7+

## 项目展示
- 系统首页
![系统首页](static\img\首页.png)
- 加载页
![加载页](static\img\加载页.png)
- 数据可视化
![数据可视化](static\img\可视化.png)
- 数据展示
![数据展示](static\img\数据展示.png)
- 模糊查询
![模糊查询](static\img\模糊查询.png)

## 安装指南

> 以下操作均是需要`Python` 环境下，在**项目文件**根目录执行

- 项目启动前需修改 `config.py` 文件中的数据库用户名与密码与本地保持一致
```bash
# 首先，确认本地python有没有安装virtualenv,如果没有执行下面一条命令
pip install virtualenv
```
```bash
# 创建虚拟解释器 env为创建的虚拟解释器名称
virtualenv env
# 切换进入虚拟解释器 
env\Scripts\activate
# 成功后会在命令行前缀出现 (env)，如果没有请检查上述步骤 
# 安装 项目依赖包   可以用国内源加速
pip install -r requirements.txt
# 用国内源加速
pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```bash
# 进入MySQL命令行中执行`51job_TABLE.sql`文件，建立项目所需的表
# 注:此操作需在MySQL命令行界面执行
source 项目文件目录/51job_TABLE.sql
```
```bash
# 启动 项目
flask run
```



## 文件结构

```
.
|-- REDEME.md				# 项目说明
|-- app.py					# 项目主文件
|-- config.py				# 项目配置文件
|-- 51job_TABLE.sql			# 数据库建库，建表的SQL文件
|-- models
|   `-- models.py			# MySQL表模板文件
|-- requirements.txt		# 项目依赖文件
|-- servers
|   |-- data.py				# 项目爬取数据的程序文件
|   |-- jinyan.py
|   |-- map.py				# 对爬取数据进行统计分析
|   |-- xinzi.py
|   `-- xueli.py
|-- static					# 静态资源文件
|   |-- HighCharts
|   |-- css
|   |-- fonts
|   |-- img
|   |   |-- backgroun.jpg	# 项目首页背景图
|   |   |-- log.ico			# 项目图标
|   |   `-- loading.gif		# 过度动画
|   `-- js
|-- templates
|   |-- base.html			# 项目导航栏主页面
|   |-- data.html			# 数据展示页面
|   |-- h.html				# 数据可视化图表页面
|   `-- input.html			# 用户输入页面
`-- venv					# 项目依赖包

```



## TODO

- [x] 根据条件，实时爬取数据

- [x] 图表展示工资发布，学历情况，工作经验

- [x] 多线程爬虫

- [x] 数据展示页的模糊搜索

- [x] 过渡动画

