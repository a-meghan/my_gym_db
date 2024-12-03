from connect_mysql import connect_database
conn, cursor = connect_database()

#Task 2
# Instead of user input, we use parameters and pass arguments to the function call
def add_workout_session(member_id, session_date, session_time, workout_type):
    if conn is not None:
        try:
            # Use INSERT to add information to the table, and use placeholders for values to be held
            query = "INSERT INTO WorkoutSessions (member_id, session_date, session_time, workout_type) VALUES (%s, %s, %s, %s)"
            values = (member_id, session_date, session_time, workout_type)
            cursor.execute(query, values)
            conn.commit()
            print("Workout session added successfully!")
  
        finally:
            cursor.close()
            conn.close()

add_workout_session(3, "2024-10-17", "0:30:00", "Rock climbing")
