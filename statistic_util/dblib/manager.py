import sqlite3, os
from typing import Iterable

class manager:
    """
    ## SQLite3を管理するやつ
    SQLコマンド知らない人でもSQLite3を扱えるようになるライブラリです。
    """

    def __init__(self, dir: str = "analytics/", name: str = "message.db"):

        self.dbfp = dir+name
        
        if (not os.path.exists(dir)):
            os.mkdir(dir)
        
        self.db = sqlite3.connect(self.dbfp)

        self.dbc = self.db.cursor()
    
    def create_table(self, table: str, args: str):
        """
        SQLite3にてテーブルを作成します。
        
        ### 例
        ```py
        from statistic_util import dblib

        db = dblib.manager()
        db.create_table('Aoi', 'name str, id int')
        # SQLコマンド: CREATE TABLE IF NOT EXISTS Aoi(name str, id int)が実行される
        ```
        """
        self.dbc.execute(f"CREATE TABLE IF NOT EXISTS {table}({args})")
        self.db.commit()
    
    def insert(self, table: str, args):
        """
        SQLite3でテーブルに内容を入れ込みます。

        ### 例
        ```py
        from statistic_util import dblib
        
        db = dblib.manager()
        db.insert('Aoi', ("あいうえお", 12345))
        ```
        """
        if (isinstance(args, tuple)):
            q = ""
            for i in range(len(args)):
                q = q+"?,"
            q = q.strip(",")
        else:
            q = "?"
            args = (args,)

        self.dbc.execute(f"INSERT INTO {table} VALUES ({q})", args)
        self.db.commit()
    
    def get_contents(self, table: str):
        """
        SQLite3でテーブル内の内容を取得します。
        
        ## 例
        ```py
        from statistic_util import dblib

        db = dblib.manager()
        print(db.get_contents('aoi'))
        # [('あいうえお', 12345)]
        """

        self.dbc.execute(f"SELECT * FROM {table}")

        return self.dbc.fetchall()
    
    def delete_table(self, table: str):
        """
        SQLite3でテーブルを削除します。

        ## 例
        ```py
        from statistic_util import dblib

        db = dblib.manager()
        db.delete_table('aoi')
        ```
        """

        self.dbc.execute(f"DROP TABLE if not exists {table}")

        self.db.commit()
    
    def rename_table(self, table: str, rename: str):
        """
        SQLite3でテーブルの名前を変更します。

        ## 例
        ```py
        from statistic_util import dblib

        db = dblib.manager()
        db.rename_table('aoi', 'nekozou')
        """
        self.dbc.execute(f"ALTER TABLE {table} RENAME TO {rename}")

        self.db.commit()
    
    def get_tables(self):
        """
        SQLite3のテーブル一覧を表示します。

        ## 例
        ```py
        from statistic_util import dblib

        db = dblib.manager()
        db.get_tables()
        # [('aoi',)]
        """
        self.dbc.execute(f"SELECT name FROM sqlite_master WHERE TYPE='table'")

        return self.dbc.fetchall()
    
    def execute(self, cmd: str, args: Iterable = None):
        """
        SQLite3でSQLコマンドを実行します。

        ## 例
        ```py
        from statistic_util import dblib

        db = dblib.manager()
        db.execute('INSERT INTO aoi VALUES (?, ?)', (8, 'aoiramen'))
        """
        if (args is None):
            self.dbc.execute(cmd)
        else:
            self.dbc.execute(cmd, args)
        
        self.db.commit()
    
    def get_cursor(self):
        return self.dbc
    
    def get_database(self):
        return self.db
    
    def get_database_fp(self):
        return self.dbfp