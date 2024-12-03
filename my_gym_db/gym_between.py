from connect_mysql import connect_database
conn, cursor = connect_database()

def get_members_in_age_range(start_age, end_age):
    if conn is not None:
        try:
            query = "SELECT * FROM members WHERE age BETWEEN %s AND %s"
            values = (start_age, end_age)
            cursor.execute(query, values)
            results = cursor.fetchall()
            for member in results:
                print(member)
            print("Members in age range retrieved successfully!")

        finally:
            cursor.close()
            conn.close()

get_members_in_age_range(18, 25)