import requests
from flask import escape



def graphqlwfs(request):
    response = requests.get('http://api.plos.org/search?q=title:DNA')
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}! '.format(escape(name)) + "Message returns {}".format(escape(response.json()))
    response = requests.get('https://api.github.com')
    if response:
        print('Success!')
    else:
        print('An error has occurred.')

    def requestInputs(url):
        pass

