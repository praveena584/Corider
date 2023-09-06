from flask import Flask

from flask_restful import Api
from flask_cors import CORS
from Corider_assignment.resources.User_resource import ListUsers
from Corider_assignment.resources.User_resource import UsersIds
from Corider_assignment.resources.User_resource import InsertData
from Corider_assignment.resources.User_resource import UpdateData
from Corider_assignment.resources.User_resource import DeleteData
app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(ListUsers,'/listusers')
api.add_resource( UsersIds,'/usersids')
api.add_resource(InsertData,'/insert')
api.add_resource(UpdateData,'/updatedata')
api.add_resource(DeleteData,'/deletedata')


if __name__=='__main__':

    app.run()

    #@app.route('/Data',methods=['POST'])
