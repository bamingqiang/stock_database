'''用户配置数据类'''
class Settings():

    def __init__(self):

        #数据库连接配置
        self.conn_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'hpl17100',
            'database': 'bamq_stock',
            'charset': 'utf8mb4', }

        # 金融数据接口库tushare的token
        self.ts_token = 'beb1591e18f85a54003e5289367171a9c7d5eeccf665ff74a461f535'

        # 数据库引擎字符串
        self.str_engine = 'mysql+pymysql://root:hpl17100@localhost:3306/bamq_stock?charset=utf8mb4'

        # 股票数据的终止日期
        self.str_end_date = '20191225'




        # ——————创建表的SQL语句——————————
        # 沪深全部股票的表，stock_basic
            # 注：字段名index两侧有个单引号''，原因index是MySql的关键字，正常情况不得用为字段名，但加上''则可以。
        self.str_create_stock_basic = 'CREATE TABLE stock_basic (' \
                                      't_index int(11) DEFAULT 0,' \
                                      'ts_code varchar(12) DEFAULT "",' \
                                      'symbol varchar(10) DEFAULT "",' \
                                      'name varchar(10) DEFAULT "",' \
                                      'area varchar(10) DEFAULT "",' \
                                      'industry varchar(50) DEFAULT "",' \
                                      'fullname varchar(50) DEFAULT "",' \
                                      'enname varchar(100) DEFAULT "",' \
                                      'market varchar(10) DEFAULT "",' \
                                      'exchange varchar(10) DEFAULT "",' \
                                      'curr_type varchar(10) DEFAULT "",' \
                                      'list_status varchar(5) DEFAULT "",' \
                                      'list_date varchar(10) DEFAULT "",' \
                                      'delist_date varchar(20) DEFAULT "",' \
                                      'is_hs varchar(5) DEFAULT "",' \
                                      'PRIMARY KEY (ts_code))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'

        # 字段名后加“_0，是为了与MySql关键字区分”
        self.str_create_stock_daily_qfq = 'CREATE TABLE stock_daily_qfq (' \
                                          'ts_index int(11) NOT NULL,' \
                                          'trade_date varchar(10) DEFAULT "" COMMENT "交易日",' \
                                          'ts_code varchar(12) DEFAULT "" COMMENT "股票代码", ' \
                                          'open decimal(10,4) DEFAULT 0.00 COMMENT "开盘价",' \
                                          'high decimal(10,4) DEFAULT 0.00 COMMENT "最高价",' \
                                          'low decimal(10,4) DEFAULT 0.00 COMMENT "最低价",' \
                                          'close decimal(10,4) DEFAULT 0.00 COMMENT "收盘价",' \
                                          'pre_close decimal(10,4) DEFAULT 0.00 COMMENT "昨日收盘价",' \
                                          'change_0 decimal(10,4) DEFAULT 0.00 COMMENT "价格变动",' \
                                          'pct_chg double(16,4) DEFAULT 0.0000 COMMENT "涨跌幅",' \
                                          'vol decimal(20,4) DEFAULT 0.00 COMMENT "成交量(手)",' \
                                          'amount double(20,4) DEFAULT 0.0000 COMMENT "成交额(千元)",' \
                                          'turnover_rate double(16,4) DEFAULT 0.0000 COMMENT "换手率",' \
                                          'volume_ratio decimal(10,4) DEFAULT 0.00 COMMENT "量比",' \
                                          'ma5 decimal(10,4) DEFAULT 0.00 COMMENT "5日均价",' \
                                          'ma_v_5 decimal(20,4) DEFAULT 0.00 COMMENT "5日均量",' \
                                          'ma10 decimal(10,4) DEFAULT 0.00 COMMENT "10日均价",' \
                                          'ma_v_10 decimal(20,4) DEFAULT 0.00 COMMENT "10日均量",' \
                                          'ma20 decimal(10,4) DEFAULT 0.00 COMMENT "20日均价",' \
                                          'ma_v_20 decimal(20,4) DEFAULT 0.00 COMMENT "20日均量",' \
                                          'ma30 decimal(10,4) DEFAULT 0.00 COMMENT "30日均价",' \
                                          'ma_v_30 decimal(20,4) DEFAULT 0.00 COMMENT "30日均量",' \
                                          'ma60 decimal(10,4) DEFAULT 0.00 COMMENT "60日均价",' \
                                          'ma_v_60 decimal(20,4) DEFAULT 0.00 COMMENT "60日均量",' \
                                          'ma120 decimal(10,4) DEFAULT 0.00 COMMENT "120日均价",' \
                                          'ma_v_120 decimal(20,4) DEFAULT 0.00 COMMENT "120日均量",' \
                                          'UNIQUE KEY uni_key(trade_date,ts_code) USING BTREE,' \
                                          'KEY (ts_code) USING BTREE)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'
