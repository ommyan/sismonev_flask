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

class RecapCByProgram(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT iuran.id_program,program.program,sum(iuran.pendapatan_iuran) as jumlah "
                "FROM iuran inner join program on iuran.id_program=program.id_program "
                "where bulan = 8 and tahun= 2017 "
                "group by program.program, iuran.id_program")
       # s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class RecapCBySegmen(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT iuran.id_segmen,segmen.segmen,sum(iuran.pendapatan_iuran) as jumlah "
                "FROM iuran inner join segmen on iuran.id_segmen=segmen.id_segmen "
                "where bulan = :bulan and tahun= :tahun "
                "group by segmen.segmen, iuran.id_segmen")
        s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)



 
 