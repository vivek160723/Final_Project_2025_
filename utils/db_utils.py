import pymysql

def get_test_data_from_db():
    # Update with your DB credentials
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='vivek@160723',
        db='testdb'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT username, password FROM login_data")
    data = cursor.fetchall()
    connection.close()
    return data
