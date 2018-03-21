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

class RecapBByProgram(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT manfaat.id_program,program.program,sum(manfaat.jumlah_pembayaran) as jumlah "
                "FROM manfaat inner join program on manfaat.id_program=program.id_program "
                "where bulan = 8 and tahun= 2017 "
                "group by program.program, manfaat.id_program")
       # s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class RecapBBySegmen(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT manfaat.id_segmen,segmen.segmen,sum(manfaat.jumlah_pembayaran) as jumlah "
                "FROM manfaat inner join segmen on manfaat.id_segmen=segmen.id_segmen "
                "where bulan = :bulan and tahun= :tahun "
                "group by segmen.segmen, manfaat.id_segmen")
        s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)



 
 