import sqlite3, os

class manager:

    def __init__(self, fp: str = "analytics/message.db"):

        self.dbfp = fp
        
        if (not os.path.exists("analytics/")):
            os.mkdir("analytics/")
        
        self.db = sqlite3.connect(self.dbfp)

        self.dbc = self.db.cursor()
    
    def create_table(self, table: str, args: str):
        """
        SQLite3にてテーブルを作成します。
        
        ### 例
        ```py
        from statistic_util import dblib

        dbMan = manager()
        dbMan.create_table('Aoi', 'name str, id int')
        # SQLコマンド: CREATE TABLE IF NOT EXISTS Aoi(name str, id int)が実行される
        """
        self.dbc.execute(f"CREATE TABLE IF NOT EXISTS {table}({args})")
        self.db.commit()
    
    def insert(self, table: str, args: tuple):
        """
        SQLite3でテーブルに内容を入れ込みます。

        ### 例
        ```py
        from statistic_util import dblib
        
        dbMan = manager()
        dbMan.insert('Aoi', ("あいうえお", 12345))
        """

        q = ""
        for i in range(len(args)):
            q = q+"?,"
        q.strip(",")

        self.dbc.execute(f"INSERT INTO {table} VALUES({q})", args)
        self.db.commit()