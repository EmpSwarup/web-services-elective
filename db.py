import pymysql

class DBConnection():

  def mysqlconnect(self):
    print("Connecting to database...")
    conn = pymysql.connect(
          host='localhost',
          user="root",
          password="",  
          db='elective' 
      )
  
    cur = conn.cursor()
    return conn,cur