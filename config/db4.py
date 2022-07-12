#source:https://www.youtube.com/watch?v=M2NzvnfS-hI
import psycopg2
db_conn=None
db_cursor=None
'''
t_host = "Nasser22-2737.postgres.pythonanywhere-services.com"
t_port = "5432" # default port for postgres server
t_dbname = "mydb"
t_name_user = "super"
t_password = "Goo@allmona_22"
'''
t_host = "localhost"
t_port = "5432" # default port for postgres server
t_dbname = "mydb"
t_name_user = "Nasser22"
t_password = "Goo@allmona_22"

try:
    db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_name_user, password=t_password)
    db_cursor = db_conn.cursor()
    #Create New Tables if they are not exists
    #Table events, and Table evtuser
    db_cursor.execute("CREATE TABLE IF NOT EXISTS usrinfo (usr_id SERIAL primary key, uname varchar(300) NOT NULL, email varchar(255),password varchar(255),created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),last_login TIMESTAMPTZ NOT NULL DEFAULT NOW())")
    db_cursor.execute("CREATE TABLE IF NOT EXISTS usrevents (evt_id SERIAL primary key, ename varchar(300) NOT NULL, sdesc varchar(500),usr_id int ,created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),last_login TIMESTAMPTZ NOT NULL DEFAULT NOW(), CONSTRAINT fk_usrinfo FOREIGN KEY(usr_id) REFERENCES usrinfo(usr_id))")
    db_cursor.execute("CREATE TABLE IF NOT EXISTS usrevents_img (imgid SERIAL primary key,img_title varchar(300) NOT NULL, img_desc varchar(500),evt_id int, created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),last_login TIMESTAMPTZ NOT NULL DEFAULT NOW(), CONSTRAINT fk_usrevents FOREIGN KEY(evt_id) REFERENCES usrevents(evt_id))")
    db_conn.commit()
    print("Login Successfully!")
except Exception as error:
    print(error)
    print("Login failed please check the error mesaage!!")
finally:
    db_cursor.close()
    db_conn.close()
    
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_name_user, password=t_password)
db_cursor = db_conn.cursor()

'''
Analysis

t_host: If your database is on a local machine, use “localhost” as the address, otherwise, an IP address.
t_port: “5432” is the default port for postgreSQL servers.
t_dbname: The name of your database.
t_name_user: The user name you set up with permissions to access the Postgres database from Python.
t_password: Password for the above user.
db_conn: Connection to your PostgreSQL server.
db_cursor: Cursor for reading/writing from/to the database with Python.
'''