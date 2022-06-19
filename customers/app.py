import re
from flask import Flask, request 
from flask_restful import Api, Resource 
import json 

app=Flask(__name__) 
api=Api(app) 

class customer(Resource):
   def get(self):
      with open ("customers.json", "r") as file:
         data=json.load(file)
      return data 

def customerName(data):
   customerList=[]
   for i in range(len(data['customers'])):
      customerList.append(data['customers'][i]['username'])
      print(data['customers'][i]['username'])
   return customerList 

def add_customer(data, username, phone, password, email): 
   new={"username":username,
   "p_details":{"email":email, "phone":phone, "password":password},
               "cart":{"items":[],
                        "paid":"False"
                     },
               "orders":[] 
      }
   data['customers']+=[new]
   return data

class addCustomer(Resource):
   def post(self):
      with open ("customers.json", "r") as file:
         data=json.load(file)
      nameList=customerName(data)
      email=request.args.get('email')
      userName=email.split('@')[0]
      if userName in nameList:
         return "User already exist" 
      name=request.args.get('name')
      phone=request.args.get('phone')
      password=request.args.get('password')
      data=add_customer(data, userName, phone, password, email) 
      json_object = json.dumps(data)
      with open("customers.json", "w") as file:
         file.write(json_object)
      return "Welcome " + name 
   
   def get(self):
      with open ("customers.json", "r") as file:
         data=json.load(file)
      return data['customers']

def addto_Cart(data,username, food, chef, quantity, price):
   customerList = customerName(data)
   if username not in customerList:
      return "Invalid Username" 
   new={"food": food,
         "chef": chef,
         "qualtity": quantity,
         "price": price
      } 
   data['customers'][customerList.index(username)]['cart']['items'] += [new] 
   return data

class addtoCart(Resource):
   def post(self):
      with open ("customers.json", "r") as file:
         data=json.load(file)
      username=request.args.get('username')
      food=request.args.get('food')
      chef=request.args.get('chef')
      quantity=request.args.get('quatity')
      price=request.args.get('price')
      data=addto_Cart(data,username, food, chef, quantity, price)
      json_object = json.dumps(data)
      with open("customers.json", "w") as file:
         file.write(json_object)
      return "Added to cart !! " 

class cart(Resource):
   def post(self):
      with open ("customers.json", "r") as file:
         data=json.load(file) 
      username=request.args.get('username')
      customerList = customerName(data)
      if username not in customerList:
         return "Invalid Username"
      return data['customers'][customerList.index(username)]['cart']['items']

def delete(data, username, food):
   for i in range(len(data['customers'][0]['cart']['items'])):
      if data['customers'][0]['cart']['items'][i]['food']=="pizza":
         del data['customers'][0]['cart']['items'][i] 
         break 
   return data

class removeItem(Resource):
   def post(self): 
      with open ("customers.json", "r") as file:
         data=json.load(file) 
      username=request.args.get('username')
      customerList = customerName(data)
      if username not in customerList:
         return "Invalid Username" 
      food=request.args.get('item')
      data=delete(data, username, food) 
      json_object = json.dumps(data)
      with open("customers.json", "w") as file:
         file.write(json_object) 
      return "removed sucessfully !! "


api.add_resource(customer,'/') 
api.add_resource(addCustomer,'/addCustomer')
api.add_resource(addtoCart, '/addtocart')
api.add_resource(cart,'/cart')
api.add_resource(removeItem,'/removeItem')


if __name__=='__main__': 
    app.run(debug=True,port=80)

