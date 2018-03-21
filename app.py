from __future__ import absolute_import 
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
from sqlalchemy.sql import text
from flask_cors import CORS



# db_connect = create_engine('sqlite:///chinook.db')
db_connect = create_engine('mysql+pymysql://homestead:secret@localhost/monev_lengkap?host=localhost?port=3306')
app = Flask(__name__)
CORS(app)
api = Api(app)

from Membership import RecapByProgram,RecapBySegmen,RecapbuByJU,RecapbuBySU
from Contribution import RecapCByProgram,RecapCBySegmen
from Benefit import RecapBByProgram,RecapBBySegmen



#membership
api.add_resource(RecapByProgram, '/peserta/program') # Route_1
api.add_resource(RecapBySegmen, '/peserta/segmen') # Route_2
api.add_resource(RecapbuByJU, '/bu/jenisbu') # Route_3
api.add_resource(RecapbuBySU, '/bu/skala') # Route_4
#Contribution
api.add_resource(RecapCByProgram, '/contrib/program') # Route_1
api.add_resource(RecapCBySegmen, '/contrib/segmen') # Route_2
#Beneffit
api.add_resource(RecapBByProgram, '/benefit/program') # Route_1
api.add_resource(RecapBBySegmen, '/benefit/segmen') # Route_2

 
if __name__ == '__main__':
     app.run(port=5000)