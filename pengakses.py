import pymysql.cursors

# Open database connection
db = pymysql.connect("localhost","root","","kampus" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      username = row[1]
      email = row[2]
      password = row[3]
      # Now print fetched result
      print ("id = %s,username = %s,email = %s,password = %d" % \
             (id, username, email, password ))
except:
   print ("Error: unable to fetch data")