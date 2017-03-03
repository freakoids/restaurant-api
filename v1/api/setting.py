#settings for database

username = 'postgres'
password = 'your_password' #replace with your password
port = '5432'
dbname = 'yourdbname' #replace with your database name
hostname = 'localhost'

URL_DB = 'postgres://{0}:{1}@{2}:5432/{3}'.format(username, password, hostname, dbname)
