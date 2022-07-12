from sqlalchemy import create_engine, MetaData
import psycopg2

DB_HOST="Nasser22-2737.postgres.pythonanywhere-services.com"
DB_NAME="mydb" 
DB_USER="Nasser22"
DB_PASS="Allmona_22"
DB_PORT="12737"

dbconn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)

cur=dbconn.cursor()
cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, stname VARCHAR(255));")

dbconn.close()