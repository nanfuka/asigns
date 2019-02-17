import psycopg2
import psycopg2.extras
import os



class DatabaseConnection:
    def __init__(self):
        self.db_name = 'kabbo'
        self.connection = psycopg2.connect(
            dbname=self.db_name, user='postgres', host='localhost',
            password='test', port=5432)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        print('Connected to the database successfully.')
        print(self.db_name)
        
    def create_users_table(self):
        create_users_table = "CREATE TABLE IF NOT EXISTS users\
        (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL,username VARCHAR NOT NULL, gender VARCHAR NOT NULL, dateofbirth VARCHAR NOT NULL, maritalstatus VARCHAR NOT NULL);"
        self.cursor.execute(create_users_table)
        self.connection.commit()
    

    def create_member(self, firstname, lastname, username, gender, dateofbirth, maritalstatus):
        query = """ INSERT INTO users (firstname, lastname, username, gender, dateofbirth, maritalstatus) VALUES ('{}', '{}', '{}', '{}','{}', '{}') 
                RETURNING userid, firstname, lastname, username, gender, dateofbirth;"""\
                .format(firstname, lastname, username, gender, dateofbirth, maritalstatus)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_members(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def get_images(self):
        query = "SELECT images FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def get_all_user_details(password):
        query = "SELECT  FROM users WHERE password = '{}'".formart(password)
        self.cursor.execute(query)
        return self.cursor.fetchone()

if __name__ == '__main__':
    db_name = DatabaseConnection()
    db_name.create_users_table()