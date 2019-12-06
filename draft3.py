import requests
import os
import graphene
import json

def fetchFeaturesFromWFS(count, typeNames, filters):
    OS_KEY = os.getenv('OS_KEY', '????????')
    wfsApiBaseUrl = "https://osdatahubapi.os.uk/OSFeaturesAPI/wfs/v1?service=wfs&request=GetFeature&key=MfGatryANoVWNLZwfkdpTFC1FWhRkwRQ&version=2.0.0&outputformat=geoJSON"
    payload = {
        'typeNames': typeNames,
        'count': count
    }

    filters = {
        'ward': "Bottisham Ward",
        'parish': "Brinkley CP"  
    }


    # TODO: generate <Filter> from filters
    for k, v in filters.items():
        if k != "" and v != "":
            filter = """
                <Filter>
                    <PropertyIsEqualTo>
                        <PropertyName>{0}</PropertyName>
                        <Literal>{1}</Literal>
                    </PropertyIsEqualTo>
                </Filter>
            """.format(k, v)
        payload["filter"] = filter
    response = requests.get(wfsApiBaseUrl, params=payload)
    return response.json()["features"]


print(fetchFeaturesFromWFS(100, typeNames, filters))
# print(fetchFeaturesFromWFS(5, "osfeatures:Sites_AccessPoint", None))
    # if response.status_code != 200:
    #     payloader = print(">>>>>>>>>>>>>>>> payload", payload)
    #     urlResponse = print(">>>>>>>>>>>>>>>> url", response.url)
    #     txtResponse = print(">>>>>>>>>>>>>>>> text", response.text)
    #     headerResp = print(">>>>>>>>>>>>>>>> headers", response.headers)
    #     statusResp = print(">>>>>>>>>>>>>>>> status_code", response.status_code)
    #     return "Error: Check your logs" 
    # return response.json()['features']

