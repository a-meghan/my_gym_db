from connect_mysql import connect_database
conn, cursor = connect_database()

#Task 1:
def get_member_info():
    # User input to gather information about new member
    name = input("Enter member's name: ")
    age = input("Enter member's age: ")
    email = input("Enter member's email: ")
    phone = input("Enter member's phone number: ")
    join_date = input("Enter member's join date (YYYY-MM-DD): ")
    expiration_date = input("Enter member's expiration date (YYYY-MM-DD): ")

    # Return the values
    return {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone,
        "join_date": join_date,
        "expiration_date": expiration_date
    }

def add_member(member_info):
    if conn is not None:
        try:
            query = "INSERT INTO members (name, age, email, phone, join_date, expiration_date) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (member_info["name"], member_info["age"], member_info["email"], member_info["phone"], member_info["join_date"], member_info["expiration_date"])
            cursor.execute(query, values)
            conn.commit()
            print("Member added successfully!")
        
        finally:
            cursor.close()
            conn.close()


member_info = get_member_info()
add_member(member_info)