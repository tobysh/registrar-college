from  flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes.hello import Hello

app = Flask(__name__)

api = Api(app)

api.add_resource(Hello, "/api/hello")
