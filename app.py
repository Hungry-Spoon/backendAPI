from flask import Flask, request
from flask_restful import Api, Resource
import json 

app=Flask(__name__) 
api=Api(app) 


def chef_name(data):
  l = len(data['chef'])
  chefList=[]
  for i in range (l) :
    chefList.append(data['chef'][i]['name'])
  return chefList

def food_list(data,chef):
  chefList=chef_name(data)
  l = len(data['chef'][chefList.index(chef)]['items'])
  food=[]
  for i in range (l) :
    food.append(data['chef'][chefList.index(chef)]['items'][i]['food'])
  return food 

def add_chef(data,chef): 
  cheflist=chef_name(data)
  newchef = {"name":chef,
        "items":[]} 
  if chef in cheflist:
    return data
  data['chef'] = data['chef'] + [newchef] 
  return data

def add_food(data, chef, food, price, available):
  chefList=chef_name(data) 
  foodList = food_list(data, chef)
  c=[
      {
        "food": food,
        "price": price,
        "isAvailable" : available,
        }
    ] 
  if food in foodList:
    data = update_item(data, chefList, price, available)
    return data
  data['chef'][chefList.index(chef)]['items']=data['chef'][chefList.index(chef)]['items'] + c 
  return data

def update_item(data, chefList, price, available) :
  data['chef'][chefList.index("kfc")]['items'][0]['price'] = price
  data['chef'][chefList.index("kfc")]['items'][0]['isAvailable'] = available 
  return data 


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
      chefList=chef_name(data)
      if chef not in chefList:
         return "First add chef " + chef
      data = add_food(data, chef, name, price, isAvailable)
      json_object = json.dumps(data)
      with open("sample.json", "w") as file:
         file.write(json_object)
      return f"Added {name} Successfully",name 
      
class addChef(Resource):
   def post(self):
      chef=request.args.get('chef')
      with open("sample.json", "r") as file:
         data = json.load(file)
      data = add_chef(data, chef)
      json_object = json.dumps(data)
      with open("sample.json", "w") as file:
         file.write(json_object)
      return "Welcome to the family " + chef
      

api.add_resource(Food,'/')
api.add_resource(addFood,'/addFood')
api.add_resource(addChef,'/addChef') 
if __name__=='__main__': 
    app.run(debug=True)

