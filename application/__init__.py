from flask import Flask

app=Flask(__name__,static_url_path='/static')

from application import routes      #import routes for the app