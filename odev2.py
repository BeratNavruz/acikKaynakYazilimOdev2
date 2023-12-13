from flask import Flask, request

from flask_restful import Api, Resource

import pandas as pd

import requests





app = Flask(__name__)

api = Api(app)



class Users(Resource):

   def get(self, sayi):

       url = "https://api.frankfurter.app/latest?amount=" + sayi + "&from=USD&to=TRY"



       response = requests.get(url)

       data = response.json()

       return {'data' : data['rates']['TRY']}, 200





api.add_resource(Users, '/users/<string:sayi>')



if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()