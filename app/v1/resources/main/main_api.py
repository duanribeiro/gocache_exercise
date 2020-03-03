from flask_restplus import Resource, Namespace
from bson.json_util import dumps
import json
from flask import request

api = Namespace('', 'Main API Endpoints')

@api.route('/main')
class MainAPI(Resource):

    def get(self):
        """
        Show the information in query string parameters
        """
        data = request.args.get('data')

        if not data:
            data = "OK!"

        return json.loads(dumps(data)), 200

