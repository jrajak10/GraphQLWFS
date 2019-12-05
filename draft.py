import requests
import os
import json
import graphene
from graphene import ObjectType, String, Schema, Argument, ID, Int, List, Field




# class Coordinates(ObjectType):
#       coordinates = List(coordinates)

class Voter(ObjectType):
      id = ID()
      name = String(required=True)
      age = Int()
      party = String()
      coordinates = List(Int)





class Query(ObjectType):
      voters = List(Voter, first = Int())
      
      def resolve_voters(self, info):
            return[
              Voter(id=10472, name="Boris", age = 55, party="Conservative", coordinates = [1, 2, 3, 6, 3]),
              Voter(id=200566, name="Jeremy", age=70, party="Labour", coordinates = [1, 2, 3, 6, 3]),
              Voter(id=572634, name="Jo", age=39, party="Lib Dems", coordinates = [1, 2, 3, 6, 3]),
              Voter(id=9836183, name="Nicola", age=49, party="SNP", coordinates = [1, 2, 3, 6, 3]),
              Voter(id=357261, name = "Jimbob", age = 25, party="Undecided", coordinates = [1, 2, 3, 6, 3])
            ]
      
            
            

 
schema = graphene.Schema(query=Query)

result = schema.execute(
  '''
  {
    voters{
      name
      id
      age
      party
      coordinates
    }
  }
  '''
)

items = dict(result.data.items())
print(json.dumps(items, indent=3))

