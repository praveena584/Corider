import pandas as pd
import pymongo
from flask import jsonify
from flask import request
import numpy as np
from flask_restful import Resource, request
# from pymongo import collection

import Corider_assignment.common.connect as config





class ListUsers(Resource):

    def get(self):
        try:

            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            # myclient = config.conn()
            print(myclient)

            mydb = myclient["mydb"]
            mycol = mydb["myc"]
            print("hello")
            for data in mycol.find():
                print(data)
                data['_id'] = str(data['_id'])

                return jsonify(data)

        except Exception as e:
            print(e, "error occurs")


class UsersIds(Resource):

    def get(self):

        global x
        try:

            myclient = pymongo.MongoClient("mongodb://localhost:27017/")

            mydb = myclient["mydb"]
            mycol = mydb["myc"]
            projection = {"id":1,"name": 1,}
            result = mycol.find({}, projection)


            for document in result:
                document['_id'] = str(document['_id'])
                print(document)
                return jsonify(document)

            # return {"res_status": True, "status": 200, "data": "UsersIds to display"}

        except Exception as e:
            print(e, "error occurs")


# Insert data
class InsertData(Resource):
    def post(self):
        try:
            data = request.get_json()

            id = data["id"]
            email = data["email"]
            name = data['name']
            password = data['password']

            myclient = pymongo.MongoClient("mongodb://localhost:27017/")

            mydb = myclient["mydb"]
            mycol = mydb["myc"]
            document_data = {"id": f'{id}',
                             "name": f'{name}',
                             # "_id": f'{_id}',
                             "email": f'{email}', "password": f'{password}'
                             }
            result = mycol.insert_one(document_data)

            print("Data Inserted Sucessfully")
            return {"res_status": True, "status": 200,
                    "msg": "**********Data inserted sucessfully**********"}
        except Exception as e:
            print(e, "error occurs")


# data updation
class UpdateData(Resource):
    def put(self):
        try:
            data = request.get_json()
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydb"]
            mycol = mydb["myc"]

            id = data["id"]
            password = data["password"]

            # email = data["email"] if data["email"] elif data['name'] else "enter"
            # update_data = data["email"] if "email" in data else ("name" in data and data["name"]) or data['password']
            # print(update_data)

            # from_date = request_data['from_date'] if request_data['from_date'] else 'DEAL_START_DATE'

            update_condition = {"id": f'{id}'}


            update_operation = {"$set": {"password": f"{password}"}}

            # Update multiple documents that match the condition
            result = mycol.update_many(update_condition, update_operation)
            print("Updated Sucessfully")
            return {"res_status": True, "status": 200,
                    "msg": "***********Data updated sucessfully**************"}
        except Exception as e:
            print(e, "error occurs")


class DeleteData(Resource):
    def post(self):
        try:
            data = request.get_json()
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydb"]
            mycol = mydb["myc"]
            name = data['name']
            print(name)
            # address=data['address']
            # print(address)
            # delete_condition = {"status": "D"}
            delete_condition = {"name": f'{name}'}

            # Define the update operation
            result = mycol.delete_many(delete_condition)

            return {"res_status": True, "status": 200,
                    "msg": "*************Data sucessfully Deleted****************"}
        except Exception as e:
            print(e, "error occurs")
