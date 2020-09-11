import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('C:/Users/KG/source/repos/CredLoggerV3/profiles.db')
        self.curs = self.conn.cursor()
        self.curs.execute('CREATE TABLE IF NOT EXISTS profiles (application, username, password, email)')

    def submit(self, application, username, password, email):
        self.curs.execute('INSERT INTO profiles (?, ?, ?, ?)', (application, username, password, email))