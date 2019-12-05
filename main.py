import requests
import os
import graphene
 
def fetchFeaturesFromWFS(count, typeNames, filters):
    OS_KEY = os.getenv('OS_KEY', '????????')
    wfsApiBaseUrl = "https://osdatahubapi.os.uk/OSFeaturesAPI/wfs/v1?service=wfs&request=GetFeature&key=MfGatryANoVWNLZwfkdpTFC1FWhRkwRQ&version=2.0.0&outputformat=geoJSON".format(OS_KEY)
    payload = {
        'typeNames': typeNames,
        'count': count
    }
    # TODO: generate <Filter> from filters
    for k, v in filters.items():
        if v != "":
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
    
    if response.status_code != 200:
        payloader = print(">>>>>>>>>>>>>>>> payload", payload)
        urlResponse = print(">>>>>>>>>>>>>>>> url", response.url)
        txtResponse = print(">>>>>>>>>>>>>>>> text", response.text)
        headerResp = print(">>>>>>>>>>>>>>>> headers", response.headers)
        statusResp = print(">>>>>>>>>>>>>>>> status_code", response.status_code)
        return "Error: Check your logs" 
    return response.json()['features']
# Getting started with GraphQL. In this way we can extract data from the query. 
# {
#     boundaryLinePollingDistrict (
#         first: 5
#         ward: "Bottisham Ward",
#         parish: "Brinkley CP"  
#     )
# }
# TODO: Next step is to convert this in a proper query.
class Query(graphene.ObjectType):
    boundaryLinePollingDistrict = graphene.String( 
      first=graphene.Int(default_value=10),
      ward=graphene.String(default_value=None),
      parish=graphene.String(default_value=None)
  )
    

    goodbye = graphene.String()

    hello = graphene.String(
        count=graphene.Int(default_value=10),
        typeNames=graphene.String(default_value="osfeatures:BoundaryLine_PollingDistrict"), 
        filters = graphene.String(default_value=None)
    )   

    def resolve_goodbye(self, info):
        return "Goodbye World"

  
    def resolve_hello(self, info, count, typeNames, filters):
        return fetchFeaturesFromWFS(10, "osfeatures:BoundaryLine_PollingDistrict", filters=filters)
        
        # return fetchFeaturesFromWFS(count, typeNames="osfeatures:BoundaryLine_PollingDistrict", filters=filters)

    def resolve_boundaryLinePollingDistrict(self, info, filters):
        filters = {
            "ward": "Bottisham Ward",
           
        }  
        return fetchFeaturesFromWFS(count=10, typeNames="osfeatures:BoundaryLine_PollingDistrict", filters=filters) 
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
    graphQlQuery = request.data.decode('utf-8')
    schema = graphene.Schema(query=Query)


    graphQlQuery = '''
     goodbye {
            goodbye

     }
    '''
    result = schema.execute(graphQlQuery)
    
    # result = schema.execute(graphQlQuery)
    #  TODO: error handling
    return result.data["goodbye"]