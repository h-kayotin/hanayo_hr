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

COOKIE = "x-zp-client-id=5a56de66-950e-4588-9ffd-0a9d262c7a6d; ssxmod_itna=YqRxBDyDuD90Kqeq0dD=nBkBD0iDc0W=QQhQPx0HnyeGzDAxn40iDt=oHO0==0=BqveEefDPhsLKROaRIe7iYauzWDCPGnDBI+bKIDYYkDt4DTD34DYDixibkxi5GRD0KDFWqvz19Dm4GWWqGfDDoDYb=RDitD4qDBGodDKqGgWM0jFCUowThqwY4cD0U3xBLNQpqczlnWgYXqVQWDThQDzMFDtLUgnkLox0p99utDZE+WKA+oSOD0/7PP+0D4fGwK7IpNQBq4RKPeBYmNfA4PYDpIavqDG+hcwiD===; ssxmod_itna2=YqRxBDyDuD90Kqeq0dD=nBkBD0iDc0W=QQhDn9Oey5DsrqoDLQ0oXS8qnRy6bMU3yiDWItPqk=07XQXQ+Q43Dw2EPGcDYK5xD===; acw_tc=276077d616916498427056806eeaea9082d2935a0e13659351dac4eecd38b6; FSSBBIl1UgzbN7NO=59HjVZiUxmujyWgFZMySLbwmyuVmi2E0aazRYe87O3eKrAZoj_ebX0r4D.PYxfrgaJSFsFgzFA_ZCB0LlRpNMzq; locationInfo_search={%22code%22:%22538%22%2C%22name%22:%22%E4%B8%8A%E6%B5%B7%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; _uab_collina=169164984401197228954184; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1691649844; zp_passport_deepknow_sessionId=3cf48dc1s91ede4f4884689127e89d6c2028; at=8bfb74ac94014060814410c62a2b05ba; rt=c87550507f6c406292ce6a6ac079ce3b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22635377275%22%2C%22first_id%22%3A%22187c668a574364-04c7645cfd1ed5-26031b51-2073600-187c668a575810%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3YzY2OGE1NzQzNjQtMDRjNzY0NWNmZDFlZDUtMjYwMzFiNTEtMjA3MzYwMC0xODdjNjY4YTU3NTgxMCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjYzNTM3NzI3NSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22635377275%22%7D%2C%22%24device_id%22%3A%22187c668a574364-04c7645cfd1ed5-26031b51-2073600-187c668a575810%22%7D; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1691649955; FSSBBIl1UgzbN7NP=5RJ1oLKsVf_lqqqDx6OAFPG.r3k.digVPKH9RXIPfGI_upvh2Fh8jALT_dz4gyrlOgPtTKTn7qYoE9QzfLpyho142v2HXm1ewAvYqXJC30yPMsw078Fk0aXhf5TXrk312jYO214sOzxXaLrH8_T1sRyqNJzv1M5G8asMZRZWCNwEHWHUxWkwC61CwNXp0oNwYxgroYLrzSMLVyL7JvIdaFiLbJXUCobAR2pnjQ_RkdMb_TAB__P.KWxahQTW7JnlOwXFb2w.cZYtjj3oUEafZkdXv8PKyBYgJsU91KcEnvlDvgor1QQ0aAmzJWp8EIxFOqGzKgsLKju7s43Ic45BmKS"

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
