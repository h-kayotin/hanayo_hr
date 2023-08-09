"""
config.py - 连接数据库

Author: kayotin
Date 2023/8/4
"""

HOST = '192.168.32.11'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'abc@1234'
DATABASE = 'hanayo_hr_db'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URI

COOKIE = "x-zp-client-id=bfc00f2a-82f0-4a01-80ad-b1754195ac13; sts_deviceid=174780cdbc0374-08ce1426227cc8-f7b1332-2073600-174780cdbc19bd; locationInfo_search={%22code%22:%22538%22%2C%22name%22:%22%E4%B8%8A%E6%B5%B7%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; selectCity_search=530; at=56ff314fe2264d0a99c7ab31c8682cb1; rt=626e848088744785a32e7e2e571f7af9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22635377275%22%2C%22%24device_id%22%3A%22174780cdbcc325-008e7173bff669-f7b1332-2073600-174780cdbcdbbb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%22174780cdbcc325-008e7173bff669-f7b1332-2073600-174780cdbcdbbb%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1Y2Q0N2Y0MmU3MWQtMGQ2MTI2NmFlNTE5YzY4LTI2MDIxMDUxLTIwNzM2MDAtMTg1Y2Q0N2Y0MmZlYjAiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI2MzUzNzcyNzUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22635377275%22%7D%7D; ssxmod_itna=7q0xRD2DcDniYY5GHQme=GAcDCu+2ig4DIdD/FmDnqD=GFDK40oEH5Tqbrb+UTPmDQuPYSbcwW3w3hQiBopIjDB3DEx0=hKAYxiiuDCeDIDWeDiDGb7DX2K0OD7qiOD7gQDLDWHCDLxYQjtqxDCrY4or=DI4GMj4DuDGtPkgNDYktDmMQDY8tDju3DKkUPcqD2FrT9DYPcYxDlYOFb+hetdwaFXLrYvjbQynRQ6ST=OZm9GwUuDYojepicWFUg7a4q7Bmjp7fxmihWe4x4GGhhKGhdebht9bh5/9Dhe4+tYgwtYB+UgveDG84TrDD===; ssxmod_itna2=7q0xRD2DcDniYY5GHQme=GAcDCu+2ig4DKG9QoYDBqfTx7pxeGOGaHohx820Kh0GaMK0Txx7YSQeqN=oH9LBteaGtmF5zcn+OAxYtwEmEU1n4M15RzEM7407mFx7=D+rbD==; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1691155580,1691413746; acw_tc=2760829f16914157520226967ea06125fbf7c16dc39e2517bf22f1972cd245; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1691415760"

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