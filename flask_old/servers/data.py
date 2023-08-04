
# 主题 + 分页 + 保存本地

from lxml import html
import requests
import pymysql
import re, random
import threading
from hanayo_hr import config

host = config.HOST
post = config.PORT
username = config.USERNAME
password = config.PASSWORD
database = config.DATABASE

etree = html.etree
tlock=threading.Lock()

db = pymysql.connect(
    host="localhost",
    port=3306,
    user=username,
    password=password,
    db=database,
    charset='utf8'
)

# 拿到游标
cursor = db.cursor()


user_agent = [

    # Firefox
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    # Safari
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    # chrome
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 "
    "(KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    # 360
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    # 猎豹浏览器
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
    "Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; "
    ".NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    # QQ浏览器
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; "
    ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; "
    ".NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)"
]


def get_user_agent():
    """随机获取一个请求头"""
    return {'User-Agent': random.choice(user_agent)}


def requst(url):
    """requests到url的HTML"""
    html = requests.get(url,headers=get_user_agent())
    html.encoding = 'gbk'
    return etree.HTML(html.text)


def get_url(url):
    data = requst(url)
    href = data.xpath('//*[@id="resultList"]/div/p/span/a/@href')
    print(len(href))
    return href


def get_data(urls):
    """获取51job职位信息,并存入数据库"""
    list_all = []
    for url in urls:
        regjob = re.compile(r'https://(.*?)51job.com', re.S)
        it = re.findall(regjob, url)
        if it != ['jobs.']:
            print('不匹配')
            continue
        try:
            data = requst(url)
            # 职位名称
            titles = data.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/@title')[0]
            # 公司
            company = data.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]/@title')[0]

            ltype = data.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title')[0]
            ltype_str = "".join(ltype.split())
            # print(ltype_str)
            ltype_list = ltype_str.split('|')
            #城市地区
            addres = ltype_list[0]
            #经验
            exper = ltype_list[1]
            # 发布日期
            if len(ltype_list)>=5:
                #学历
                edu = ltype_list[2]
                dateT = ltype_list[4]
            else:
                #学历
                edu = "没有要求"
                dateT = ltype_list[-1]
            # 薪资
            salary = data.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()')
            if len(salary) == 0:
                salary_list = [0,0]
            else:
                salary_list = salary_alter(salary)[0]
            # 招聘详情
            contents = data.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div')[0]
            content = contents.xpath('string(.)')
            # content = content.replace(' ','')
            content = "".join(content.split())

            list_all.append([titles,company,addres,salary_list[0],salary_list[1],dateT,edu,exper,content])
            item = [titles, company, addres, salary_list[0], salary_list[1], dateT, edu, exper, content]
            write_db(item)
        except:
            print('爬取失败')


def write_db(data):
    """写入数据库"""
    print(data)
    try:
        tlock.acquire()
        # rows变量得到数据库中被影响的数据行数。
        rescoun = cursor.execute(
            "insert into data (post,company,address,salary_min,salary_max,dateT,edu,exper,content) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
        # 向数据库提交
        db.commit()
        tlock.release()
        # 如果没有commit()，库中字段已经向下移位但内容没有写进，可是自动生成的ID会自动增加。
        print('成功')
        global db_item
        db_item = db_item + 1

    except:
        # 发生错误时回滚
        db.rollback()
        tlock.release()
        print('插入失败')


def get_cityid(city):
    try:
        tlock.acquire()
        cursor.execute("select city_id from city where city_name='%s'" % city)
        city_id = cursor.fetchone()
        # 向数据库提交
        db.commit()
        tlock.release()
        if city_id == None:
            return '000000'
        else:
            return city_id[0]
    except:
        # 发生错误时回滚
        db.rollback()
        print("查询失败")
        return 0


def salary_alter(salarys):   #[]
    salary_list = []
    for salary in salarys:
        # print(salary)
        if salary == '':
            a = [0,0]
        re_salary = re.findall('[\d+\.\d]*', salary)  # 提取数值--是文本值
        salary_min = float(re_salary[0])  # 将文本转化成数值型,带有小数，用float()

        wan = lambda x,y : [x*10000,y*10000]
        qian = lambda x, y: [x * 1000, y * 1000]
        wanqian = lambda x,y,s :wan(x,y) if '万' in salary else qian(x,y)
        tian = lambda x, y, s: [x,y] if '元' in salary else qian(x, y)

        if '年' in salary:
            salary_max = float(re_salary[2])
            a = wanqian(salary_min,salary_max,salary)
            a[0] = round(a[0] / 12, 2)
            a[1] = round(a[1] / 12, 2)
        elif '月' in salary:
            salary_max = float(re_salary[2])
            a = wanqian(salary_min, salary_max, salary)
        elif '天' in salary:
            salary_max = float(re_salary[0])
            a = tian(salary_min, salary_max, salary)
            a[0] *= 31
            a[1] *= 31
        salary_list.append(a)
    return salary_list

def data_clr():
    # 清空data
    try:
        tlock.acquire()
        query = "truncate table `data`"
        cursor.execute(query)
        db.commit()
        tlock.release()
        print('data原表已清空')
    except Exception as aa:
        print(aa)
        print('无data表！')


def main(kw, city,startpage):
    print(kw)
    print(city)
    city_id = get_cityid(city)
    print(city_id)
    data_clr()
    page = startpage
    global db_item
    db_item = 0
    while(db_item <= 200):
        url = "https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html".format(city_id,kw,page)
        print(url)
        # url = 'https://search.51job.com/jobsearch/search_result.php'
        a =get_url(url)
        print(a)
        get_data(a)
        page = page + 1
        print(db_item)
        # time.sleep(0.2)
if __name__ == '__main__':
    main('PHP','山东',1)
