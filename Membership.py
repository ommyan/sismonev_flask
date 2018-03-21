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

class RecapByProgram(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT cakupan.id_program,program.program,sum(cakupan.jumlah_peserta) as jumlah "
                "FROM cakupan inner join program on cakupan.id_program=program.id_program "
                "where bulan = 8 and tahun= 2017 "
                "group by program.program, cakupan.id_program")
        s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class RecapBySegmen(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT cakupan.id_segmen,segmen.segmen,sum(cakupan.jumlah_peserta) as jumlah "
                "FROM cakupan inner join segmen on cakupan.id_segmen=segmen.id_segmen "
                "where bulan = :bulan and tahun= :tahun "
                "group by segmen.segmen, cakupan.id_segmen")
        s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class RecapbuByJU(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT cakupan_bu.id_jenis_bu,jenis_bu.jenis_bu,sum(cakupan_bu.jumlah_bu) as jumlahbu "
                "FROM cakupan_bu inner join jenis_bu on cakupan_bu.id_jenis_bu=jenis_bu.id_jenis_bu "
                "where bulan = :bulan and tahun= :tahun and cakupan_bu.id_program= 1 "
                "group by jenis_bu.jenis_bu, cakupan_bu.id_jenis_bu ")
        s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class RecapbuBySU(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT cakupan_bu.id_skala,skala_bu.skala,sum(cakupan_bu.jumlah_bu) as jumlahbu "
                "FROM cakupan_bu inner join skala_bu on cakupan_bu.id_skala=skala_bu.id_skala "
                "where bulan = :bulan and tahun= :tahun and cakupan_bu.id_program= 1 "
                "group by skala_bu.skala, cakupan_bu.id_skala")
        s= s.bindparams(bulan='8', tahun='2017')        
        query=conn.execute(s)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

 
 