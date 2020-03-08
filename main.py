
import tushare as ts                        # 加载tushare类库，金融接口类库，方便获取金融数据。
import functions as fc
from settings import Settings
import time
import pandas as pd

my_settings = Settings()

# ——————————————————调试区————————————————————————————————————————————




# ——————————————————调试区————————————————————————————————————————————

# 获取数据库引擎
db_engine = fc.get_db_engine(my_settings.str_engine)

# 设定数据连接和游标
db_conn = fc.get_db_conn(my_settings.conn_config)
db_cursor = fc.get_db_cursor(db_conn)

# 初始化tushare
ts.set_token(my_settings.ts_token)
pro = ts.pro_api()                          #　以上两行，初始化tushare，设置个人的token用于访问类库的数据接口

# 因股票经常变化，每次启动清空股票表stock_basic，再获取数据股票明细，存入stock_basic表
# fc.drop_table(db_conn, db_cursor, 'stock_basic')
# fc.create_table(db_conn, db_cursor, my_settings.str_create_stock_basic)
# fc.empty_table(db_conn, db_cursor, 'stock_basic')
# fc.get_stock_basic(pro, db_engine)    # 获取基本股票数据
# fc.empty_table(db_conn, db_cursor, 'stock_daily_qfq')
# fc.drop_table(db_conn,db_cursor,'stock_daily_hfq')
# fc.create_table(db_conn, db_cursor, my_settings.str_create_stock_daily_qfq)
# db_cursor.close()
# db_conn.close()
# exit()

# ——————————————————调试区————————————————————————————————————————————
'''
str_sql = 'select * from stock_basic;'
db_cursor.execute(str_sql)
rows_stock = db_cursor.fetchall()
data = pd.DataFrame(list(rows_stock))
data.to_csv(r'f:\basic.csv')
exit()
'''
# ——————————————————调试区————————————————————————————————————————————

# 从stock_basic表中获取股票数据
str_sql = 'select ts_code, list_date from stock_basic;'
db_cursor.execute(str_sql)
rows_stock = db_cursor.fetchall()

current_date = str(int(time.strftime("%Y%m%d", time.localtime())))  # 格式化获取当前日期 20190128
for row in rows_stock:      # 逐个股票获取日线数据
    stock_code = row[0]
    list_date = row[1]
    fc.get_daily_qfq(ts, db_engine, db_cursor, stock_code, list_date, current_date)

db_cursor.close()
db_conn.close()
exit()

