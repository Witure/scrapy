import pymysql


class ssmy():
    def __init__(self,ip,root,paw,dbname):
        self.ip = ip
        self.root = root
        self.paw = paw
        self.dbname = dbname


    def content(self):
        #建立连接
        self.db = pymysql.connect(self.ip,self.root,self.paw,self.dbname)
        #拿到游标
        self.cursor = self.db.cursor()



    def close(self):
        self.cursor.close()
        self.db.close()


    def get_version(self):
        self.cursor.execute('select version()')
        self.data = self.cursor.fetchone()
        return self.data


    def get_one(self,tname):
        self.tname = tname
        self.cursor.execute('select * from '+self.tname)
        self.data = self.cursor.fetchone()
        return self.data


    def get_all(self,tname):
        self.tname = tname
        self.cursor.execute('select * from ' + self.tname)
        self.data = self.cursor.fetchall()
        return self.data














