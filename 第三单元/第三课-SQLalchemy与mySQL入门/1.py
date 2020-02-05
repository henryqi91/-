from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Column, String, Integer

engine = create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/test",
    max_overflow=5,   #超过连接池大小，最多可以创建的链接
    pool_size=10,     #连接池大小
    echo=True         #调试信息展示
)

metadata = MetaData()

user = Table(
    'user', metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(10))
)

metadata.create_all(engine)
