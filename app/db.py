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
        
    # def create_users_table(self):
    #     create_users_table = "CREATE TABLE IF NOT EXISTS users\
    #     (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL,username VARCHAR NOT NULL, gender VARCHAR NOT NULL, dateofbirth VARCHAR NOT NULL, maritalstatus VARCHAR NOT NULL);"
    #     self.cursor.execute(create_users_table)
    #     self.connection.commit()

    def create_users_table(self):
        create_users_table = "CREATE TABLE IF NOT EXISTS users (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL,username VARCHAR NOT NULL, gender VARCHAR NOT NULL, dateofbirth VARCHAR NOT NULL, maritalstatus VARCHAR NOT NULL,churchfamily VARCHAR, fellowshipgroup VARCHAR, leadershiprole VARCHAR, highestlevelofeducation VARCHAR, profession VARCHAR, occupation VARCHAR, placeofwork VARCHAR, placeofresidence VARCHAR, phonecontact VARCHAR, emailaddress VARCHAR, dateofbaptism VARCHAR, placeofbaptism VARCHAR, nameofpastorwhobaptised VARCHAR, formerreligion VARCHAR);"      
        self.cursor.execute(create_users_table)
        self.connection.commit()

    # def create_users_table(self):
    #     create_users_table = "CREATE TABLE IF NOT EXISTS users\
    #     (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL,username VARCHAR NOT NULL, gender VARCHAR NOT NULL, dateofbirth VARCHAR NOT NULL, maritalstatus VARCHAR NOT NULL);"
    #     self.cursor.execute(create_users_table)
    #     self.connection.commit()

    # def create_users_table(self):
    #     create_users_table = "CREATE TABLE IF NOT EXISTS users\
    #     (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL,username VARCHAR NOT NULL, gender VARCHAR NOT NULL, dateofbirth VARCHAR NOT NULL, maritalstatus VARCHAR NOT NULL);"
    #     self.cursor.execute(create_users_table)
    #     self.connection.commit()
    

    def create_member(self, firstname, lastname, username, gender, dateofbirth, maritalstatus, churchfamily, fellowshipgroup, leadershiprole, highestlevelofeducation, profession, occupation, placeofwork, placeofresidence, phonecontact, emailaddress, dateofbaptism, placeofbaptism, nameofpastorwhobaptised, formerreligion):
        query = """ INSERT INTO users (firstname, lastname, username, gender, dateofbirth, maritalstatus, churchfamily, fellowshipgroup, leadershiprole, highestlevelofeducation, profession, occupation, placeofwork, placeofresidence, phonecontact, emailaddress, dateofbaptism, placeofbaptism, nameofpastorwhobaptised, formerreligion) VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}','{}') 
                RETURNING firstname, lastname, username, gender, dateofbirth, maritalstatus, churchfamily, fellowshipgroup, leadershiprole, highestlevelofeducation, profession, occupation, placeofwork, placeofresidence, phonecontact, emailaddress, dateofbaptism, placeofbaptism, nameofpastorwhobaptised, formerreligion;"""\
                .format(firstname, lastname, username, gender, dateofbirth, maritalstatus, churchfamily, fellowshipgroup, leadershiprole, highestlevelofeducation, profession, occupation, placeofwork, placeofresidence, phonecontact, emailaddress, dateofbaptism, placeofbaptism, nameofpastorwhobaptised, formerreligion)
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

    def get_details_for_particularuser(self, username):

        # query = "SELECT * FROM incidents WHERE incident_type = '{}' AND incident_id = {};".format(
        #     incident_type, incident_id)

        query = "SELECT * FROM users WHERE username = '{}';".format(username)
        self.cursor.execute(query)
        return self.cursor.fetchone()
    def edit_data(self, userId, item, newvalue):
        query = """UPDATE users SET {} = '{}'  WHERE userId = {}  RETURNING userId;""".format(item, newvalue, userId)
        self.cursor.execute(query)
        return self.cursor.fetchone()
    def delete_member(self, username):
        query = "DELETE * FROM users WHERE username = '{}';".format(username)
    def get_all_user_ids():
        query = "SELECT userId from users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_usernames():
        query = "SELECT username from users"
        self.cursor.execute(query)
        return self.cursor.fetchall()


if __name__ == '__main__':
    db_name = DatabaseConnection()
    db_name.create_users_table()