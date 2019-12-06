import requests
import os
import json
import graphene
from graphene import ObjectType, String, Schema, Argument, ID, Int, List, Field, Float
from collections import namedtuple

geojson = {
    type: "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
            "type": "Polygon",
            "coordinates": [
            [
            [
            459661.0700000003,
            1210427.52
            ],
            [
            459650.8300000001,
            1210431
            ],
            [
            459657.71,
            1210450.42
            ],
            [
            459644.3099999996,
            1210455.23
            ],
            [
            459650.0300000003,
            1210470.4
            ],
            [
            459673.79,
            1210461.57
            ],
            [
            459661.0700000003,
            1210427.52
            ]
            ]
            ]
            },
            "properties": {
            "OBJECTID": 1,
            "SHAPE_Length": 123.563607102599,
            "SHAPE_Area": 633.100400019014
            }
            },
            {
            "type": "Feature",
            "geometry": {
            "type": "Polygon",
            "coordinates": [
            [
            [
            459713.1699999999,
            1210222.720000001
            ],
            [
            459706.5999999996,
            1210225.24
            ],
            [
            459715.5099999998,
            1210248.449999999
            ],
            [
            459722.0800000001,
            1210245.93
            ],
            [
            459713.1699999999,
            1210222.720000001
            ]
            ]
            ]
            },
            "properties": {
            "OBJECTID": 2,
            "SHAPE_Length": 63.7963420255192,
            "SHAPE_Area": 174.942899996946
            }
        }
    ]
}


class Geometry(ObjectType):
    type = String()
    coordinates = List(Float)
    ObjectID = ID()
    
class Properties(ObjectType):
    ObjectID = ID()
    Shape_Length = Float()
    Shape_Area = Float()


class Feature(ObjectType):
    type = String()
    geometry = Field(Geometry)
    properties = Field(Properties)
    ObjectID = ID()



def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(geojson):
    return json.loads(geojson, object_hook=_json_object_hook)
    
x = json2obj(geojson)

print(x)

class Query(ObjectType):
    features = List(Feature, id=Int(required=True))

    def resolve_features(self, args, context, info):
        features =  geojson["features"]
        return json2obj(json.dumps(features))

