import mysql.connector
from mysql.connector import errorcode


class connector:
    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(host=host, user=user,
                                                password=password, database=database)
            if self.conn.is_connected():
                self.cursor = self.conn.cursor(dictionary=True)
                print('DB is connected')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("user name or password is wrong")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def Create(self, sql: str):
        self.cursor.execute(sql)
        self.conn.commit()

    def Update(self, sql: str):
        self.cursor.execute(sql)
        self.conn.commit()

    def Read(self, sql: str) -> {}:
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def Delete(self, sql: str):
        self.cursor.execute(sql)
        self.conn.commit()