from sqlalchemy import create_engine, MetaData
import psycopg2

#SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://Nasser22-2737.postgres.pythonanywhere-services.com:12737"
#BASE_PATH = '/home/Nasser22/mydb/'

#DB_HOST="Nasser22-2737.postgres.pythonanywhere-services.com:12737"
#DB_NAME="mydb" 
#DB_USER="Nasser22"

#DB_PASS="Allmona_22"

#dbconn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)


#dbconn.close()


#First we need to pass the connection string as a parameter to the create_engine function.
#The Server and Port properties must be set to a MySQL server.
#Use the create_engine function to create an Engine for working with MySQL data.
#engine =create_engine("mysql+pymysql://root@localhost:3306/test")
#engine = create_engine("mysql+pymysql://?User=Nasser22&;Password=Pyt@allmona_22&Database=Nasser22$mydb&Server=Nasser22.mysql.pythonanywhere-services.com&Port=3306")
#engine = create_engine(SQLALCHEMY_DATABASE_URI)
t_host = "localhost"
t_port = "5432" # default port for postgres server
t_dbname = "mydb"
t_name_user = "Nasser22"
t_password = "Goo@allmona_22"
DATABASE_URL = "postgresql://Tabook22:Allmona_22@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
#engine = create_engine('postgresql://Nasser22:Allmona_22@Nasser22-2737.postgres.pythonanywhere-services.com:12737/mydb')

meta=MetaData()
conn=engine.connect() 

#If IntegratedSecurity is set to false, then User and Password must 
# be set to valid user credentials. Optionally, Database can be 
# set to connect to a specific database. If not set, tables from all 
# databases will be returned.