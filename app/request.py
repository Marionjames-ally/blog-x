import urllib.request,json
from .models import Quotes

base_url  = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_BASE_URL']

def get_quotes(quotes):
    '''
    Function that gets the json responce to our url request
    '''
    get_quotes_url = base_url(quotes)
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        quotes_result = None
        if get_quotes_response['results']:
            quotes_result_list =get_quotes_response['results'] 
            quote_result = process_results(quotes_result_list)
    

    return quotes_result