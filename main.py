import requests
# from flask import escape
# import json 



def graphqlwfs(url):
    url = "https://osdatahubapi.os.uk/OSFeaturesAPI/wfs/v1?service=wfs&request=GetCapabilities&key=pxKGVMtaA9X2382DdJA4h3hAi6mkXt60&version=2.0.0"
    filterRequest = "&typenames=osfeatures:BoundaryLine_PollingDistrict&outputformat=geoJSON"
    count = 20

    newUrl = str(url.replace("GetCapabilities", "GetFeature") + filterRequest + "&count=" + str(count))
    response = requests.get(newUrl)
    # """HTTP Cloud Function.
    # Args:
    #     request (flask.Request): The request object.
    #     <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    # Returns:
    #     The response text, or any set of values that can be turned into a
    #     Response object using `make_response`
    #     <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    # """
    # request_json = request.get_json(silent=True)
    # request_args = request.args

    # if request_json and 'name' in request_json:
    #     name = request_json['name']
    # elif request_args and 'name' in request_args:
    #     name = request_args['name']
    # else:
    #     name = 'World'

    features = response.json()

    return features

    
