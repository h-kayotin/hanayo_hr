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

COOKIE = """
    x-zp-client-id=bfc00f2a-82f0-4a01-80ad-b1754195ac13; sts_deviceid=174780cdbc0374-08ce1426227cc8-f7b1332-2073600-174780cdbc19bd; ssxmod_itna=QqAxB7GQqTqBPxeuT4jxCwp76G8mlFQffDBdlxiNDnD8x7YDvzCNDGgogt2M9DwosimDYv1A/1qc2pP6WnnRCWDCPGnDB9GerzDYYODt4DTD34DYDirQGy8qBQDjxAQDjGKGaDfTtGcDYjjiT4DCOG4XO=DI4GMU4DuDGUPOxiDYwtDmq=DY+tDjM3DKwtKyqD2WOu9DYpcUxDlUh9kGgIt=LcF2u2YEnRQglb=X4n=kcey+LtnDYEjK60cFztS8a54Qox4zG3dz0qWKi4q3+GkK7w3m7GkS04oYAkobih+eozYRhsXPD===; acw_tc=2760828c16911555697792899e392c74152c2df33fea05d046c152a492ebed; locationInfo_search={%22code%22:%22538%22%2C%22name%22:%22%E4%B8%8A%E6%B5%B7%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1691155580; zp_passport_deepknow_sessionId=cfa16bcfsc5eb24e5b93e81d2383b4302702; selectCity_search=530; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1691156103; at=56ff314fe2264d0a99c7ab31c8682cb1; rt=626e848088744785a32e7e2e571f7af9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22635377275%22%2C%22%24device_id%22%3A%22174780cdbcc325-008e7173bff669-f7b1332-2073600-174780cdbcdbbb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%22174780cdbcc325-008e7173bff669-f7b1332-2073600-174780cdbcdbbb%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1Y2Q0N2Y0MmU3MWQtMGQ2MTI2NmFlNTE5YzY4LTI2MDIxMDUxLTIwNzM2MDAtMTg1Y2Q0N2Y0MmZlYjAiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI2MzUzNzcyNzUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22635377275%22%7D%7D; sts_sg=1; sts_evtseq=1; sts_sid=189c0c59ac9448-01b54a9a11740f-26031c51-2073600-189c0c59acab26; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fpassport.zhaopin.com%2F; ZP_OLD_FLAG=false
"""