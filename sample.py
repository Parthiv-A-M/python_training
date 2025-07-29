"""#age = int(input("Enter your age"))
#if age<10:
#    print("Child")
#else:
#   print("Adult")

cars=["Ford", "Volvo","BMW","TATA"]
print(len(cars))
print(cars[3])

for i in range(len(cars)):
    print(cars[i])

for i in cars:
    print(i) """

"""list = ["one","two","three"]
print(list[0])

print(list[5])
except Exception as e:
    print("error in array")  
    print("this is the last line")

with open("sample.txt",'w') as file:
    file.write ("from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Display the current date and time
print("Current Date and Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
")"""

import mysql.connector
def insert_data(id,name,email):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="rene_ece"
    )
    mycursor = mydb.cursor()
    sql = "insert into norah(id,name,email)""values (%s,%s,%s)"
    val = [id,name,email]
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record insert")

id = input("enter the id")
name = input("enter the name")
email = input("enter the email")
insert_data(id,name,email)


