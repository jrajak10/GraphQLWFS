import requests
<<<<<<< HEAD
=======
import os

>>>>>>> 62249c30947aa640d2b485fa81042c3ff1457514
"""HTTP Cloud Function.
Args:
    request (flask.Request): The request object.
    <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
Returns:
    The response text, or any set of values that can be turned into a
    Response object using `make_response`
    <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
"""
def graphqlwfs(request):
<<<<<<< HEAD
    wfsApiBaseUrl = "https://osdatahubapi.os.uk/OSFeaturesAPI/wfs/v1?service=wfs&request=GetFeature&key=MfGatryANoVWNLZwfkdpTFC1FWhRkwRQ&version=2.0.0&outputformat=geoJSON"
=======
    OS_KEY = os.getenv('OS_KEY', '????????')
    wfsApiBaseUrl = "https://osdatahubapi.os.uk/OSFeaturesAPI/wfs/v1?service=wfs&request=GetFeature&key={}&version=2.0.0&outputformat=geoJSON".format(OS_KEY)
>>>>>>> 62249c30947aa640d2b485fa81042c3ff1457514
    # request_json = request.get_json(silent=True)
    typeNames = request.args.get("typeNames", default="osfeatures:BoundaryLine_PollingDistrict")
    count = request.args.get("count", default=100)
    PropertyName = request.args.get("PropertyName", default=None)
    Literal = request.args.get("Literal", default=None)
    payload = {
        'typeNames': typeNames,
        'count': count
    }
    if PropertyName != None and Literal != None:
        filter = """
                <Filter>
                    <PropertyIsEqualTo>
                        <PropertyName>{0}</PropertyName>
                        <Literal>{1}</Literal>
                    </PropertyIsEqualTo>
                </Filter>
            """.format(PropertyName, Literal)
        payload["filter"] = filter
    response = requests.get(wfsApiBaseUrl, params=payload)
    payloader = print(">>>>>>>>>>>>>>>> payload", payload)
    urlResponse = print(">>>>>>>>>>>>>>>> url", response.url)
    txtResponse = print(">>>>>>>>>>>>>>>> text", response.text)
    headerResp = print(">>>>>>>>>>>>>>>> headers", response.headers)
    statusResp = print(">>>>>>>>>>>>>>>> status_code", response.status_code)
    if response.status_code != 200:
        return "Please enter a typeName!!! " + str(urlResponse) + str(txtResponse) + str(headerResp) + str(PropertyName) + str(Literal) +str(payload)
    else:
        features = response.json()
    return features
    # if status_code != 200:
    #     return "NOOOOOO!!!"
    # #     return response.json()
<<<<<<< HEAD
    # return response.json()
=======
    # return response.json()
>>>>>>> 62249c30947aa640d2b485fa81042c3ff1457514
