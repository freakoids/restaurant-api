from flask import Flask , make_response, jsonify
from sqlalchemy.orm import sessionmaker
from api.models.model import init_db
from api.setting import URL_DB
from flask_httpauth import HTTPBasicAuth
#global variables
app = Flask(__name__)

engine = init_db(URL_DB)
Session = sessionmaker(bind=engine)


auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
	if username == 'admin':
		return 'admin'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'eroor' : 'Unauthorized access'}), 401)




@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error' : 'Not found'}), 404)

from api import endpoints
from api import utilityendpoints, customerendpoints, employeeendpoints, billendpoints
from api import dailyendpoints
