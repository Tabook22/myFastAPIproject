import psycopg2
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='Nasser22', ssh_password='Allmona_22',
    remote_bind_address=('Nasser22-2737.postgres.pythonanywhere-services.com',12737)
) as tunnel:
    db_conn = psycopg2.connect(
        user='super', password='Goo@allmona_22',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='mydb',
    )
    cur = db_conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS events (evt_id SERIAL primary key, ename varchar(300) NOT NULL, sdesc varchar(500),created_on TIMESTAMP NOT NULL,last_login TIMESTAMP)")
    db_conn.commit()
   
    db_conn.close()
    