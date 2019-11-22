import requests

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
    wfsApiBaseUrl = "https://osdatahubapi.os.uk/OSFeaturesAPI/wfs/v1?service=wfs&request=GetFeature&key=pxKGVMtaA9X2382DdJA4h3hAi6mkXt60&version=2.0.0&outputformat=geoJSON"
    # request_json = request.get_json(silent=True)
<<<<<<< HEAD
    typeNames = request.args.get("typeNames", default="")
    count = request.args.get("count", default=100)
    PropertyName = request.args.get("PropertyName", default="")
    propertyValue = request.args.get("propertyValue", default="")
    payload = {
        'typeNames': typeNames,
        'count': count
    }
    if property == "" or propertyValue == "":
        filter = """
            <Filter>
                <PropertyIsEqualTo>
                    <PropertyName>{0}</PropertyName>
                    <Literal>{1}</Literal>
                </PropertyIsEqualTo>
            </Filter>
        """.format(PropertyName, propertyValue)
        payload["filter"] = filter
    response = requests.get(wfsApiBaseUrl, params=payload)
    print(">>>>>>>>>>>>>>>> payload", payload)
    print(">>>>>>>>>>>>>>>> url", response.url)
    print(">>>>>>>>>>>>>>>> text", response.text)
    print(">>>>>>>>>>>>>>>> headers", response.headers)
    print(">>>>>>>>>>>>>>>> status_code", response.status_code)
    if status_code != 200:
        // TODO parse XML which is in response.text
        return "NO NO NOc ccccc"
    else:
        features = response.json()
        return features
=======
    typeNames = request.args.get("typeNames", default="osfeatures:BoundaryLine_PollingDistrict")
    count = request.args.get("count", default=100)
    propertyName = request.args.get("propertyName", default=None)
    propertyValue = request.args.get("propertyValue", default=None)
    payload = {
        'typeNames': typeNames,
        'count': count,
        'propertyName': propertyName,
        "propertyValue": propertyValue
    }
    if propertyName == "" or propertyValue == "":
        filter = """
                <Filter>
                    <PropertyIsEqualTo>
                        <propertyName>{0}</propertyName>
                        <Literal>{1}</Literal>
                    </PropertyIsEqualTo>
                </Filter>
            """.format(propertyName, propertyValue)
        payload["filter"] = filter
    response = requests.get(wfsApiBaseUrl, params=payload)
    payloader = print(">>>>>>>>>>>>>>>> payload", payload)
    urlResponse = print(">>>>>>>>>>>>>>>> url", response.url)
    txtResponse = print(">>>>>>>>>>>>>>>> text", response.text)
    headerResp = print(">>>>>>>>>>>>>>>> headers", response.headers)
    statusResp = print(">>>>>>>>>>>>>>>> status_code", response.status_code)
    if response.status_code != 200:
        return "Please enter a typeName!!! " + str(urlResponse) + str(txtResponse) + str(headerResp) + str(propertyName) + str(propertyValue) +str(payload) 
    else:
        features = response.json()
    return features

    # if status_code != 200:
    #     return "NOOOOOO!!!"
    # #     return response.json()
    # return response.json()
>>>>>>> parameters
