from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json 

app=Flask(__name__) 
api=Api(app) 

def add_food(d, key, value, isa):
    d[key] = {"price": value, "isAvailable": isa}
    return d

class Food(Resource): 
   def get(self):
      with open('sample.json', 'r') as openfile:
         json_object = json.load(openfile)
      return json_object 

class addFood(Resource):
   def post(self):
      chef=request.args.get('chef')
      name = request.args.get('name') 
      price = request.args.get('price')
      isAvailable = request.args.get('isAvailable') 
      with open("sample.json", "r") as file:
         data = json.load(file)
      for i in data.keys():
         if i == chef:
            data[chef]=add_food(data[chef], name, price, isAvailable)
      json_object = json.dumps(data)
      with open("sample.json", "w") as file:
         file.write(json_object)
      return json_object
      
class addChef(Resource):
   def post(self):
      chef=request.args.get('chef')
      chefList=[]
      with open("sample.json", "r") as file:
         data = json.load(file)
      for i in data.keys():
         chefList.append(i)
      if chef not in chefList:
            data[chef]={}
      json_object = json.dumps(data)
      with open("sample.json", "w") as file:
         file.write(json_object)
      return json_object
      

api.add_resource(Food,'/chef')
api.add_resource(addFood,'/addFood')
api.add_resource(addChef,'/addChef') 
if __name__=='__main__': 
    app.run(debug=True)

