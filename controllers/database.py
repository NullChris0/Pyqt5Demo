import sqlite3

class Database:
    def __init__(self, db_file, schema_file):
        print(db_file)
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        with open(schema_file, 'r', encoding='utf-8') as file:
            script = file.read()
        self.cursor.executescript(script)
        self.conn.commit()
        rows = script.splitlines()
        if len(rows) > 50:  # 第一次运行后销毁插入数据的段落
            changed_script = '\n'.join(rows[:50])
            with open(schema_file, 'w', encoding='utf-8') as file:
                file.write(changed_script)

    def execute_query(self, query, params=None):
        '''执行数据库操作并返回受影响的行数'''
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def fetch_dicts(self, query, params=None):
        self.cursor.execute(query, params or ())
        key = [column[0] for column in self.cursor.description]
        return [dict(zip(key, row)) for row in self.cursor.fetchall()]

    def get_member(self, param):
        '''根据姓名或电话号码获取会员信息，两个属性同时进行模糊查询，返回字典'''
        self.cursor.execute("SELECT * FROM Member WHERE name = ? OR phone = ?", (param, param))
        key = [column[0] for column in self.cursor.description]
        value = self.cursor.fetchone()
        if value:
            return dict(zip(key, value))
        else:
            return None
    
    def get_rules(self):
        # 获取充值规则，大额在前
        return sorted(self.fetch_all('SELECT * FROM RechargeRules'), key=lambda x: x[1], reverse=True)

    def close(self):
        self.cursor.close()
        self.conn.close()