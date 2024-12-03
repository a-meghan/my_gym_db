from connect_mysql import connect_database
conn, cursor = connect_database()

def delete_workout_session(session_id):
    if conn is not None:
        try:
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))
            conn.commit()
            print("Workout session deleted successfully!")

        finally:
            cursor.close()
            conn.close()

delete_workout_session(2)