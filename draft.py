import requests
import os
import json
import graphene
from graphene import ObjectType, String, Schema, Argument, ID, Int, List



class Voter(ObjectType):
      id = ID()
      name = String(required=True)
      age = Int()
      party = String()


class Query(ObjectType):
      voters = List(Voter, first = Int())
      
      def resolve_voters(self, info, first):
            return[
              Voter(id=10472, name="Boris", party="Conservative"),
              Voter(id=200566, name="Jeremy", age=70, party="Labour"),
              Voter(id=572634, name="Jo", age=39, party="Lib Dems"),
              Voter(id=9836183, name="Nicola", age=49, party="SNP")
            ][:first]
      
            
            

 
schema = graphene.Schema(query=Query)

result = schema.execute(
  '''
  {
    voters(first:2) {
      id
      name
      age
      party
    }
  }
  '''
)

items = dict(result.data.items())
print(json.dumps(items, indent=3))

