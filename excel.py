# import pandas as pd
#
# data_frame = pd.DataFrame(((2, 3, 4), (5, 6, 7)))
# print(data_frame)
# col = pd.DataFrame(('a', 'b', 'c')).T
# print(col)
# frame = pd.DataFrame(data_frame, columns=['a','b','c'])
# print(frame)
import pandas as pd
import pandas.io.sql as sql
import pymysql as ps


def connect_database(host, port, user, password, db):
    # 连接数据库，返回cursor对象
    connection = ps.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset='utf8mb4',
        autocommit=True,
    )
    return connection


# conn是数据库的连接对象
dataframe = sql.read_sql('select * from EMP', connect_database('192.168.1.111', 3306, 'root', '123', 'study'))
print(pd.DataFrame(dataframe.values))
