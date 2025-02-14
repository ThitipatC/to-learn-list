from flask_restful import Resource, Api,request
import json
from utilities.genAI import generateList
class Task(Resource):

    def post(self):
        if request.headers.get("Content-Type") != "application/json":
            return {"msg" : "unsupported content type"}, 400
        body = json.loads(request.data)
        if "topic" not in body:
            return {"msg" : "Please provide the topic field inside the body"}, 400 
        res = json.loads(generateList(body["topic"]))
        return {"data": res}, 200