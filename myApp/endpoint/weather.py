import pdb
from flask import Blueprint, jsonify, request
from myApp.database import getDb
import requests

weatherEndpoint = Blueprint('weather', __name__)

@weatherEndpoint.route('/weather/list')
def getWeather():

    if not request.args['city']:
        return jsonify({});

    url = ' http://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': request.args['city'] + ',br',
        'APPID': 'c6c4012c481dc67e8438162183c9fbfa',
        'units': 'metric',
        'lang': 'pt_br'
    }
    getDb().insert_one({'consult': request.args['city']})

    return requests.get(url, params).json()

@weatherEndpoint.route('/weather/history')
def getHistory():
    consultList = []
    for consultDict in getDb().find({}, {'_id': 0, 'consult': 1}):
        consultList.append(consultDict.get('consult'))

    return jsonify({'consults': consultList})