from connect_mysql import connect_database
conn, cursor = connect_database()

#Task 3
def update_member_email(member_id, new_email):
    if conn is not None:
        try:
            # Update members and SET new email as 'placeholder' WHERE the member_id is 'placeholder'
            query = "UPDATE members SET email = %s WHERE member_id = %s"
            cursor.execute(query, (new_email, member_id))
            conn.commit()
            print("Member email updated successfully!")

        finally:
            cursor.close()
            conn.close()


update_member_email(2, "avalyn@email.com")