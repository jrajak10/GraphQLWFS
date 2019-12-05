# test = {
#         "features": [
#         {
#         "geometry": {
#                 "coordinates": [
#                 []
#                 ],
#                 "type": "Polygon"
#                 },
#                 "properties": {
#                 "County": "Cambridgeshire County",
#                 "DistricBo": "East Cambridgeshire District",
#                 "OBJECTID": 1,
#                 "PDID": "MB1",
#                 "Parish": "Brinkley CP",
#                 "Shape_Area": 5272151.0999484,
#                 "Shape_Length": 19387.6762277671,
#                 "Ward": "Bottisham Ward"
#                 },
#         "type": "Feature"
#         },
#         {
#         "geometry": {
#         "coordinates": [],
#         "type": "Polygon"
#         },
#         "properties": {
#         "County": "Cambridgeshire County",
#         "DistricBo": "East Cambridgeshire District",
#         "OBJECTID": 2,
#         "PDID": "MC1",
#         "Parish": "Burrough Green CP",
#         "Shape_Area": 9194231.54815388,
#         "Shape_Length": 24606.1294937802,
#         "Ward": "Woodditton Ward"
#         },
#         "type": "Feature"
#         },
#         {
#         "geometry": {
#         "coordinates": [
#         []
#         ],
#         "type": "Polygon"
#         },
#         "properties": {
#         "County": "Cambridgeshire County",
#         "DistricBo": "East Cambridgeshire District",
#         "OBJECTID": 3,
#         "PDID": "KE1",
#         "Parish": "Swaffham Bulbeck CP",
#         "Shape_Area": 16634471.1208801,
#         "Shape_Length": 30053.3515926216,
#         "Ward": "Bottisham Ward"
#         },
#         "type": "Feature"
#         },
#         {
#         "geometry": {
#         "coordinates": [],
#         "type": "Polygon"
#         },
#         "properties": {
#         "County": "Cambridgeshire County",
#         "DistricBo": "East Cambridgeshire District",
#         "OBJECTID": 4,
#         "PDID": "KF1",
#         "Parish": "Swaffham Prior CP",
#         "Shape_Area": 19795957.7677361,
#         "Shape_Length": 29107.9340306923,
#         "Ward": "Bottisham Ward"
#         },
#         "type": "Feature"
#         },
#         {
#         "geometry": {
#         "coordinates": [],
#         "type": "Polygon"
#         },
#         "properties": {
#         "County": "Cambridgeshire County",
#         "DistricBo": "East Cambridgeshire District",
#         "OBJECTID": 5,
#         "PDID": "KD1",
#         "Parish": "Reach CP",
#         "Shape_Area": 4593376.56030286,
#         "Shape_Length": 9931.02889781183,
#         "Ward": "Bottisham Ward"
#         },
#         "type": "Feature"
#         }
#         ],
#         "type": "FeatureCollection"
#         }

# testList = test["features"]
# lst =[]


# for i in testList:
#     if i["properties"]["Ward"] == "Bottisham Ward":
#         lst.append(i)

# print(lst)


property = "H"
propertyValue = "44"

    
filterString = "&filter=<Filter><PropertyIsEqualTo><PropertyName>" + str(property) + "</PropertyName><Literal>" + str(propertyValue) + "</Literal></PropertyIsEqualTo></Filter>"

if property == "":
        filterString = ""
if propertyValue == "":
        filterString = ""

print(filterString)    


requests = ["count", "typenames", "property", "propertyValue"]
