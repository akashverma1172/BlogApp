from turtle import pos
from mysql.connector import connect, Error
from hashlib import sha256


auth = {'host':'192.168.1.102', 'database':'socialnetworktest', 'user':'root', 'password':'NG;9bwHA'}

#Create post using this function
def CreatePost(blog_header, published_date, publisher_id, content):
    try:
        connection = connect(**auth)

        if connection.is_connected():
            print("Connected to MySQL version ", connection.get_server_info())
            
            sql_query = "INSERT INTO post (header, published_date, publisher_id, content) VALUES (?,?,?,?)"
            vals = (blog_header, published_date, publisher_id, content)
            cursor = connection.cursor()
            cursor.execute(sql_query, vals)
            connection.commit()
    except Error as conn_err:
        print("Unable to connect to database server ", conn_err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Server closed successfully")

#View the post having post id as parameter
def ViewPost(post_id):
    try:
        connection = connect(**auth)

        if connection.is_connected():
            print("Connected to DB successfully")
            sql_query = f"SELECT * FROM post WHERE post_id={post_id}"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            post_data = cursor.fetchall()
            print(post_data)
            post_data = {
                "id" : post_data[0][0],
                "header": post_data[0][1],
                "published_date": post_data[0][2],
                "publisher_id": post_data[0][3],
                "content": post_data[0][4]
            }

            return post_data
            

    except Error as conn_err:
        print("Unable to connect to database server ", conn_err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Server closed successfully")

#Search if the user wich given username exists or not
def FindUser(username):
    try:
        connection = connect(**auth)
        if connection.is_connected():
            sql_query = f"SELECT * FROM user WHERE username='{username}'"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            user_info = cursor.fetch_all()
            if(user_info):
                user_info ={
                    "user_id": user_info[0],
                    "user_fname": user_info[1],
                    "user_mname": user_info[2],
                    "user_lname": user_info[3],
                    "username": user_info[4],
                    "email": user_info[5],
                    "password_hash": user_info[6],
                    "dob": user_info[7],
                    "join_date": user_info[8],
                    "primium_user": user_info[9]
                }
                return user_info
            else:
                return None
    except Error as conn_err:
        print("Unable to connect to database server ", conn_err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Server closed successfully")

# Authenticate user
def AuthenticateUser(username, password):
    isAuthenticated = False
    password = sha256(password.encode()).hexdigest()
    user_data = FindUser(username)
    if(user_data != None):
        if(user_data["password_hash"] == password and user_data["username"] == username):
            isAuthenticated = True

    return isAuthenticated


# initialize user table
def CreateUserTable():
    try:
        connection = connect(**auth)
        if connection.is_connected():
            sql_query = """
                CREATE TABLE IF NOT EXISTS user(
                    user_id INT AUTO_INCREMENT,
                    user_fname VARCHAR(32) NOT NULL,
                    user_mname VARCHAR(32),
                    user_lname VARCHAR(32) NOT NULL,
                    username VARCHAR(64) NOT NULL,
                    email VARCHAR(64) NOT NULL,
                    user_password VARCHAR(256) NOT NULL,
                    user_dob DATE NOT NULL,
                    user_date_of_join DATE NOT NULL,
                    user_premium BOOLEAN NOT NULL,
                    
                    PRIMARY KEY(user_id)
                );
            """
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
    except Error as conn_err:
        print("Unable to connect to database server ", conn_err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Server closed successfully")

# Initialize blog table
def CreateBlogTable():
    try:
        connection = connect(**auth)
        if connection.is_connected():
            sql_query = """
                CREATE TABLE IF NOT EXISTS Post(
                    post_id INT AUTO_INCREMENT,
                    header VARCHAR(128) NOT NULL,
                    publish_date DATE NOT NULL,
                    publisher_id INT NOT NULL, 
                    content TEXT NOT NULL,
                    PRIMARY KEY(post_id),
                    FOREIGN KEY (publisher_id) REFERENCES user(user_id)
                );
            """
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
    except Error as conn_err:
        print("Unable to connect to database server ", conn_err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Server closed successfully")