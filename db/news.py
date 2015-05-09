import torndb


class NewsModel():
    def __init__(self,db):
        self.db = db
        self.table_name = "news"

    def get_all_news(self):
        sql = "SELECT * FROM %s" % (self.table_name)
        return self.db.get(sql)

class EmailModel():
    def __init__(self,db):
        self.db = db
        self.table_name = "email"

    def add_new_email(self,email):
        sql = "INSERT INTO %s ( email ) VALUES ( '%s' )" % (self.table_name,email)
 