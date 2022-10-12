import os #import os to use docker compose yaml environment variables
from psycopg_pool import ConnectionPool

# variable = ConnectionPool object ('conninfo' is the param we use provide the connection information for our pool) 
pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"]) #used to get connections to the DB
