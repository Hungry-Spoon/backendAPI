import json

with open("customers.json") as file:
   data = json.load(file)

# print(data['customers'][0]['username'])

# print((len(data['customers'])))

# for i in range(len(data['customers'])):
#    print(data['customers'][i]['username'])


def customers_name(data):
   customerList=[]
   for i in range(len(data['customers'])):
      customerList.append(data['customers'][i]['username'])
      print(data['customers'][i]['username'])
   return customerList 

# a=customers_name(data)
# print(a)


# def add_customer(data, username, phone, password, email): 
#    new={"username":username,
#    "p_details":{"email":email, "phone":phone, "password":password},
#                "cart":{"items":[],
#                         "paid":"False"
#                      },
#                "orders":[] 
#       }
#    data['customers']=data['customers']+[new]
#    return data
   
# print(add_customer(data, "bc", "78945121", "45132adsa", "bc@gmail.com"))

# print(data['customers'])

# a="abc@gmail.com"
# print(a.split('@')[0])


# print(data['customers'][0]['cart']['items']) 
# def addtoCart(data,username, food, chef, quantity, price):
#    customerList = customers_name(data)
#    new={"food": food,
#          "chef": chef,
#          "qualtity": quantity,
#          "price": price
#       } 
#    data['customers'][customerList.index(username)]['cart']['items'] += [new] 
#    return data
#    print(data['customers'][0]['cart']['items'])


# addtoCart(data,"abc", "pizza","abb","2", "78") 
def delete(data, username, food):
   for i in range(len(data['customers'][0]['cart']['items'])):
      if data['customers'][0]['cart']['items'][i]['food']=="pizza":
         del data['customers'][0]['cart']['items'][i] 
         break 
   return data
 
