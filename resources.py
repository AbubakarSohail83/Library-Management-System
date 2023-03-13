from flask import request, Response, jsonify,json
from flask_restful import Resource
from model import db


class showStudentsApi(Resource):
    def get(self):
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        studentsData=dbb.showStudents()
        json_object = json.dumps(studentsData, indent = 4)
        return Response(json_object,mimetype="application/json",status=200)

class booksApi(Resource):
    def get(self):
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        existingBooks=dbb.getlistOfBooks()
        json_object = json.dumps(existingBooks)
        return Response(json_object,mimetype="application/json",status=200)

class updateBook(Resource):
    def post(self,id):
        dbb=db("localhost","root","abubakar786","libraryManagmen")
        newData=request.get_json()
        print(newData)
        return {'id':str(id)},200