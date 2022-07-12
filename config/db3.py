import pandas as pd
import sqlalchemy

SQLALCHEMY_DATABASE_URI = "postgresql://super:Nasser22-2737.postgres.pythonanywhere-services.com:12737/mydb"
BASE_PATH = '/home/Nasser22/mydb/'

db = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)

#df = pd.read_sql(sql = 'SELECT * FROM mydb', con = db.engine)
#print("In The Name of Allah")