import pymysql

def mysqlconnect():
  print("Connecting to database")
  conn = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db='elective' 
    )
  
  cur = conn.cursor()
  query = "SELECT * FROM users;"
  cur.execute(query)
  output = cur.fetchall()
  print(output)
  
  conn.close()
  
if __name__ == "__main__":
  mysqlconnect()