import urllib.request,json
from .models import Quotes

base_url  = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_BASE_URL']
