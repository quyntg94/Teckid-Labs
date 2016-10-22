from mongoengine import connect
#mongodb://<dbuser>:<dbpassword>@ds063856.mlab.com:63856/a5-tumblelog

db_name = "a5-tumblelog"
host = "ds063856.mlab.com"
port = 63856
username = "admin"
password = "admin"

db_instance = None

def mlab_connect():
    global db_instance
    db_instance = connect(db=db_name, host=host, port=port, username=username, password=password)

def mlab_disconnect():
    db_instance.close()