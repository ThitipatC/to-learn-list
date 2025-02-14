# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
from routes.Tasks import Task
# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 
  
  
  
  
# adding the defined resources along with their corresponding urls 
api.add_resource(Task, '/tasks/generate-topics') 
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 