from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
from sqlalchemy.sql import text
 
# db_connect = create_engine('sqlite:///chinook.db')
db_connect = create_engine('mysql+pymysql://homestead:secret@localhost/monevL?host=localhost?port=3306')
app = Flask(__name__)
api = Api(app)

class RecapByProgram(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database 
        s = text(
            "SELECT program.program,sum(cakupan.jumlah_peserta) as jumlah "
                "FROM cakupan, program "
                "WHERE cakupan.id_program = program.id_program"
                "AND cakupan.bulan <= :bulan "
                "AND cakupan.tahun <= :tahun"
                "AND cakupan.id_program = :program "
                "group by cakupan.id_program,program.program")
        query=conn.execute(s, bulan='3', tahun='2017', program='1').fetchall()
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result) # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
 
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        
 
api.add_resource(RecapByProgram, '/program') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
 
 
if __name__ == '__main__':
     app.run(port=5002)