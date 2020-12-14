
import pandas as pd
import sys
import requests 
import psycopg2



class DBBot():
    '''한 프로세스에서 거래 실행하고 나면 거래 결과를 저장하는 곳'''
    def __init__(self, name):
        ##DB 기본내용 작성
        self.host = '211.218.53.149'
        self.dbname = ''
        self.user = ''
        self.pwd = ''
        self.name = name
        self.port = '5432'
        self.get_connect_info()

    def get_connect_info(self):
            self.dbname = 'NH'
            self.user = 'NH'
            self.pwd = 'nh123'
            self.port = '5432'
    def get_connection(self):
        # print("port", self.port)
        conn = psycopg2.connect('host={0} dbname={1} user={2} password={3} port={4}'.format(self.host, self.dbname, self.user, self.pwd, self.port))
        cur = conn.cursor()
        return conn, cur
    
    def execute_query(self, query):
        try:
            conn, cur = self.get_connection()
            cur.execute(query) 
            conn.commit()
            return cur
        except Exception as e:
            print("*******Error********" + str(e))
            pass
 
    def insert_order(self, trade_id, Iscd):
        query = f'''INSERT INTO trade_ids ("trade_id", "iscd")
                VALUES ('{trade_id}', '{Iscd}');
            '''   
        self.execute_query(query) 
        
    def insert_order(self, trade_id, Iscd, trade_time):
        query = f'''INSERT INTO trade_ids ("trade_id", "iscd", "trade_time")
                VALUES ('{trade_id}', '{Iscd}', {trade_time});
            '''   
        self.execute_query(query) 
        
    def get_trade_ids(self, Iscd, start_time = ''):
        '''데이터베이스의 모든 trade_history가져옴'''
        table_name = "trade_ids"
        
        query = f'''SELECT * FROM {table_name}'''

        query = query + f" WHERE iscd = '{Iscd}'"
        
        if start_time != '':
            query = query + f' and trade_time >= {start_time}'
            
        cur = self.execute_query(query)
        colnames = [desc[0] for desc in cur.description]
        a = cur.fetchall()

        return pd.DataFrame(a, columns = colnames)