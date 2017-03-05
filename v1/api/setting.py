#settings for database

username = 'postgres'
password = 'postgres' #replace with your password
port = '5432'
dbname = 'restaurant' #replace with your database name
hostname = 'localhost'

URL_DB = 'postgres://{0}:{1}@{2}:5432/{3}'.format(username, password, hostname, dbname)
