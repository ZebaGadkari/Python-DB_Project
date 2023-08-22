import sqlite3

def get_adhar_details(aadhar_no):
    connection = sqlite3.connect('adharcard.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM ADHAR WHERE adhar_no = ?', (aadhar_no,))
    result = cursor.fetchone()

    connection.close()

    return result

def main():
    user_input_aadhar_no = input("Enter the Aadhar number you want to check: ")


    adhar_details = get_adhar_details(user_input_aadhar_no)

    if adhar_details:
     if str(adhar_details[0]) ==  user_input_aadhar_no:
            print("its a valid adhar no")
            print("Aadhar Number:", adhar_details[0])
            print("Dose:", adhar_details[8])
            print("name:", adhar_details[1])
            print("age:", adhar_details[2])
        
           
     else:
            print("invalid adhar no.")
    else:
                  print("Aadhar number  does not exist in the table.")

if __name__ == "__main__":
    main()
