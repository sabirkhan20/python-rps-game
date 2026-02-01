# import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="admin",
#     database="hospital"
# ) 

# if(con.is_connected()):
#     print("Database connected successffully")

# cursor = con.cursor()
# cursor.execute("create table apolo(id int(10),pateintname varchar(50), bill int(10))")
# cursor.execute("insert into apolo(id,pateintname,bill) values(101,'Amit',120000),(102,'Anurag',12000)")
# con.commit()
# cursor.execute("Select * from apolo")
# result = cursor.fetchall()

# for i in result:
#     print(i)


# con.close()


# if (con.is_connected()):
#     print("database is connected in SQL")


# cursor=con.cursor()
# # cursor.execute("create a table city hpospital(id int(10),paitentname varchar (20), bill int(20)")
# # cursor.execute("insert into city hospital (id,paitent name,bill) values(101,'ajay',1200),(102,'anurag,1200")
# # con.commit ()
# cursor .execute ("select * from city hospital")
# result = cursor.fetchall ()

# for i in result:
#     print(i)

# con.close()

# import mysql.connector

# con = mysql.connector.connect(host="localhost", user="root", password="admin", database="hospitaldeatils")

# if con.is_connected():
#     print("Database is connected in SQL")

# cursor = con.cursor()

# Uncomment after creating the database and table
# cursor.execute("CREATE TABLE city_hospital(id INT, patientname VARCHAR(20), bill INT)")
# cursor.execute("INSERT INTO city_hospital(id, patientname, bill) VALUES (101, 'Ajay', 1200), (102, 'Anurag', 1200)")
# con.commit()

# cursor.execute("SELECT * FROM city_hospital")
# result = cursor.fetchall()

# for i in result:
#     print(i)

# con.close()

