import mysql.connector as my

con = my.connect(
    host="localhost",
    user="root",
    password="prerit",
    database='xyz'
)

cr = con.cursor()
# cr.execute("create database XYZ")
cr.execute("create table student (id int , name varchar(20))")
# cr.execute("select * from student")
# cr.execute("insert into student values(1,'Prerit')")

cr.execute("insert into student (id,name) values(2,'Prerit')")

n = input("Enter name: ")
a = int(input("Enter age: "))
data = [n,a]
cr.execute("insert into student (name,age) value(%s, %s), data")
con.commit()
print("data inserted")