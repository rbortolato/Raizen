from flask import Flask
from myApp.endpoint.weather import weatherEndpoint

app = Flask('__name___')
app.register_blueprint(weatherEndpoint)