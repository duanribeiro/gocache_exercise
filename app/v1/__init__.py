from flask import Blueprint
from flask_restplus import Api

v1_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(v1_blueprint,
          doc='/docs',
          title='Documentação Exercício Gocache',
          version='1.0',
          description='')

from .resources.main.main_api import api as main_api
api.add_namespace(main_api)