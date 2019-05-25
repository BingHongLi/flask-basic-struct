
from pymongo import MongoClient
from flask import Flask, request, abort, jsonify
application = Flask(__name__)

@application.route('/db',methods=['GET'])
def hello_world():
    hostName = request.args.get('host')
    client = MongoClient(host=hostName, port=27017, username='root', password='example')
    return str(client.list_database_names())

@application.route('/',methods=['GET'])
def index():

    return "ok"

if __name__ == '__main__' :
    application.run()