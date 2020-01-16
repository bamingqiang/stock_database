'''保存相关设置的模块'''
import pymysql
from sqlalchemy import create_engine


def get_db_engine(str_engine):
    pymysql.install_as_MySQLdb()  # 如无此两行代码，create_engine()报错ModuleNotFoundError: No module named 'MySQLdb'

    # create_engine说明
    # create_engine("mysql+pymysql://【此处填用户名】:【此处填密码】@【此处填host】:【此处填port】/【此处填数据库的名称】?charset=utf8")
    return create_engine(str_engine)


def get_db_conn(conn_config):
    return pymysql.connect(**conn_config)

def get_db_cursor(conn):
    return conn.cursor()

def empty_table(conn, cursor, str_table_name):
    str_sql = 'truncate table ' + str_table_name + ';'
    cursor.execute(str_sql)
    conn.commit()

def drop_table(conn, cursor, str_table_name):
    str_sql = 'drop table ' + str_table_name + ';'
    cursor.execute(str_sql)
    conn.commit()

def create_table(conn, cursor, str_create_table):
    cursor.execute(str_create_table)
    conn.commit()

# 获取股票数据
def get_stock_basic(pro, db_engine):
    # 调用tushare的stock_basic()方法，获取股票列表（DataFrame格式）
    data_list = pro.stock_basic(fields='ts_code,symbol,name,area,industry,fullname,'
                                       'enname,market,exchange,curr_type,list_status,'
                                       'list_date,delist_date,is_hs')
    # 给DataFrame对象的索引加名，为MySql数据库中表的字段名，DataFrame默认的索引名index与MySql的关键冲突，无法建立表
    data_list.index.name = 't_index'
    # 在数据库中创建表stock_basic，存储股票列表
    # data_list.to_csv(r'f:\aaaa.csv')
    data_list.to_sql('stock_basic', db_engine, if_exists='append')

# 获取单支股票的日线数据
def get_daily_qfq(ts, db_engine, db_cursor, stock_code, list_date, current_date ):
    str_sql = 'select max(trade_date) from stock_daily_qfq where ts_code="%s";' % stock_code
    db_cursor.execute(str_sql)          # 获取当前股票，日线表里已下载数据的最后日期
    row_daily = db_cursor.fetchone()
    if row_daily[0]:                    # 如果已经取过当前股票数据，则info[0]有数据为True，否则无数据为False
        start_date = str(int(row_daily[0]) + 1)      # 如果取过数据，则在取过的最后日期基础增加1天
    else:
        start_date = list_date          # 未取过，将即将获取数据的起始日期设为上市日期

    if int(start_date) >= int(current_date):    # 如果开始日期已经在于现在日期，则退出函数
        return

    end_date = str(int(start_date) + 100000)    # 一次取十年的数据
    if int(end_date) > int(current_date):       # 如果计算出的终止日期超过当日期，则终止日期为当前日期
        end_date = current_date
    fuquan_adj = 'qfq'              # 后复权


    # 因tushare的接口限制，每分钟取数200次，每次取4000条数据，计算需要取数多少次
    i_years = int(current_date[:4]) - int(start_date[:4]) + 1       # 计算上市了多少年，每10年取一次
    if i_years % 10 > 0:
        i_years = int(i_years / 10) + 1
    else:
        i_years = int(i_years / 10)

    for i in range(i_years):                                   # 取每10年的日线数据
        print(stock_code + '-->' + str(i) + '-->' + start_date + '-->' + end_date)

        data_daily_qfq_son = ts.pro_bar(ts_code=stock_code, adj=fuquan_adj, start_date=start_date,
                                    end_date=end_date,ma=[5,10,20,30,60,120], factors=['tor', 'vr'])

        if data_daily_qfq_son is None or len(data_daily_qfq_son) == 0:
            if i == 0:
                return
            else:
                break

        data_daily_qfq_son.index.name = 'ts_index'              # 给索引起个字段名，避免写入mysql时出错
        data_daily_qfq_son.rename(columns={'change': 'change_0'}, inplace=True)     # change为mysql的关键字，不可作字段名，改个名
        if i == 0:
            data_daily_qfq = data_daily_qfq_son
        else:
            data_daily_qfq = data_daily_qfq.append(data_daily_qfq_son)
        start_date = str(int(start_date) + 100000 + 1)          # 因为每10年，所以每取完一个十年，就要更新一下日期
        end_date = str(int(start_date) + 100000 -1)

        if int(end_date) > int(current_date):
            end_date = current_date
        if int(start_date) >= int(current_date):
            break
    data_daily_qfq = data_daily_qfq.sort_values(by=['trade_date'])
    # data_daily_qfq.to_csv(r'f:\aaaa' + '.csv')
    data_daily_qfq.to_sql('stock_daily_qfq',db_engine, if_exists='append')


