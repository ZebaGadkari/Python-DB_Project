import sqlite3
import re
from datetime import datetime

# Establish the connection
connection = sqlite3.connect('adharcard.db')

# Creating cursor
cursor = connection.cursor()

# Creating table
cursor.execute('''CREATE TABLE IF NOT EXISTS ADHAR 
               (adhar_no INTEGER PRIMARY KEY NOT NULL,
               name VARCHAR(30) ,
               age INTEGER,
               mobile_no INTEGER,
               dob DATE,
               email_id TEXT,
               gender VARCHAR(6),
               address TEXT,
               dose INTEGER
               )''')

while True:
    adhar_no = input("Enter 12-digit Aadhar number: ")
    if len(adhar_no) == 12 and adhar_no.isdigit():
        break
    else:
        print("Invalid Aadhar number")

while True:
    name = input("Enter your name: ")
    if all(char.isalpha() or char in " -'" for char in name) and 2 <= len(name) <= 30:
        break
    else:
        print("Invalid name")

while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 17:
            print("You are under 18 years old. Not eligible.")
        else:
            break
    except ValueError:
        print("Invalid age")

while True:
    mobile_no = input("Enter your mobile number: ")
    if mobile_no.isdigit() and len(mobile_no) == 10:
        break
    else:
        print("Invalid mobile number")

while True:
    dob = input("Enter your date of birth (dd-mm-yyyy): ")
    try:
        dob_datetime = datetime.strptime(dob, '%d-%m-%Y')
        break
    except ValueError:
        print("Invalid date format. Use dd-mm-yyyy")

while True:
    email_id = input("Enter email address: ")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email_id):
        break
    else:
        print("Invalid email address")

while True:
    gender = input("Enter gender (Male/Female/Other): ").lower()
    allowed_genders = ['male', 'female', 'other']
    if gender in allowed_genders:
        break
    else:
        print("Invalid gender")

address = input("Enter address: ")

while True:
    dose = input("Enter number of vaccine doses: ")
    if len(dose) <= 2 and dose.isdigit():
        break
    else:
        print("Invalid input")

# Inserting values
cursor.execute('''INSERT INTO ADHAR (adhar_no, name, age, mobile_no, dob, email_id, gender, address, dose)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
               (adhar_no, name, age, mobile_no, dob_datetime, email_id, gender, address, dose))
connection.commit()

# Display inserted data
data = cursor.execute('''SELECT * FROM ADHAR''')
for row in data:
    print(row)

# Close the connection
connection.close()
