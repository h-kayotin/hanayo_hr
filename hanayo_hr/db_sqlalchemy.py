"""
db_sqlalchemy - 用拼接字符串的方式来写sql语句操作数据库，感觉不太优雅。所以尝试下用Sqlalchemy库推荐的方式来写

参考了https://yifei.me/note/2652

Author: hanayo
Date： 2024/5/14
"""
from sqlalchemy.orm import DeclarativeBase, Session

from hanayo_hr.config import COOKIE, user_agent, DATABASE, USERNAME, PASSWORD, HOST, DB_URI

from sqlalchemy import create_engine, text
from sqlalchemy import select, update
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import Integer, String, func, UniqueConstraint

# 创建连接
engine = create_engine(
    DB_URI,  # "mysql+pymysql://{USERNAME}:{pwd_alchemy}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4",
    echo=False,  # echo 设为 True 会打印出实际执行的 sql，调试的时候更方便
    future=True,  # 使用 SQLAlchemy 2.0 API，向后兼容
    pool_size=5,  # 连接池的大小默认为 5 个，设置为 0 时表示连接无限制
    pool_recycle=3600,  # 设置时间以限制数据库自动断开
)

# 直接执行sql语句，这部分和pymysql区别不大
sql_text = "select * from tb_keys"
with engine.connect() as conn:
    result = conn.execute(text(sql_text))
    # 查询结果result类似生成器, 只能遍历一遍, 遍历第二遍时就是空数据
    # print(result.all())
    res = result.all()

# result可以遍历，每一行是一个row对象,类似具名元祖(namedtuple)，支持以下2种遍历方式
for row in res:
    print(row.keys_id, row.keys_name, row.keys_count)  # 通过字段名获取
    # print(row[0], row[1], row[2])  # 通过索引获取
print("*"*40)

# 可用以下方式执行多条
# with engine.connect() as conn:
#     data = [{"keys_id": 11, "keys_name": 'test1', "keys_count": 1},
#             {"keys_id": 12, "keys_name": 'test2', "keys_count": 1}]
#     conn.execute(
#         text("INSERT INTO tb_keys (keys_id, keys_name, keys_count) VALUES (:keys_id, :keys_name, :keys_count)"),
#         data
#     )
#     # 手动commit
#     conn.commit()


# 声明式api
class Base(DeclarativeBase):
    """DeclarativeBase无法直接使用，所以要先继承一个Base类"""
    pass


class TableCount(Base):
    __tablename__ = "tb_keys"
    keys_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    keys_name: Mapped[str] = mapped_column(String(30), index=True)
    keys_count: Mapped[int] = mapped_column(Integer)


# 用声明式API进行select查找，而不是直接执行sql语句
with Session(engine) as session:
    stmt = select(TableCount).where(TableCount.keys_count == 1).order_by(TableCount.keys_id)
    result = session.execute(stmt)
    # 一般情况下，当选取整个对象的时候，都要用 scalars 方法
    res2 = result.scalars()
    for row in res2:
        print(row.keys_id, row.keys_name, row.keys_count)
    print("*" * 40)
    # 查询单个属性，不需要用
    res3 = session.execute(select(TableCount.keys_name))
    for row in res3:
        print(row.keys_name)
    print("*" * 40)

    # 查询主键有一个快捷方式，以下查询id是7
    key_word = session.get(TableCount, 7)
    print(key_word.keys_name)

    # 更新数据使用update
    stmt = update(TableCount).where(TableCount.keys_name == "护士").values(keys_name="护师").\
        execution_options(synchronize_session="fetch")
    session.execute(stmt)

    # 也可以直接修改值，比如上面获取到的
    key_word.keys_name = "Nurse"
    session.commit()

    # 注意，以下两种方式都能更新count值，但更推荐第二种做法。第一种方式可能会导致竞争更新，race condition（竞态条件
    # key_word.keys_count += 1
    key_word.keys_count = TableCount.keys_count + 1
    session.commit()

    # 新增
    # new_word = TableCount()
    # new_word.keys_count = 0
    # new_word.keys_name = "Alice"
    # session.add(new_word)
    # session.commit()

    # 删除， 用session.delete 删除，先获取到id，在get到该对象，然后用session.delete删除
    del_word = session.execute(select(TableCount.keys_id).where(TableCount.keys_name == 'Alice')).fetchone()
    del_word_id = del_word[0]
    del_word_obj = session.get(TableCount, del_word_id)
    session.delete(del_word_obj)
    session.commit()


