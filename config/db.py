from sqlalchemy import create_engine, MetaData

#First we need to pass the connection string as a parameter to the create_engine function.
#The Server and Port properties must be set to a MySQL server.
#Use the create_engine function to create an Engine for working with MySQL data.
engine =create_engine("mysql+pymysql://root@localhost:3306/test")
meta=MetaData()
conn=engine.connect() 

#If IntegratedSecurity is set to false, then User and Password must 
# be set to valid user credentials. Optionally, Database can be 
# set to connect to a specific database. If not set, tables from all 
# databases will be returned.