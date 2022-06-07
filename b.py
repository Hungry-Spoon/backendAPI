# import json
  
# # Opening JSON file
# with open('sample.json', 'r') as openfile:
  
#     # Reading from json file
#     json_object = json.load(openfile)
  
# print(json_object)




# d = {
#   "kfc": {
#     "pizza": "400"
#   },
#   "trail": {
#     "pizza": "78 "
#   }
# }
# def add(d, key, value):
#     d[key] = value
#     return d 

# if d.keys == "c" : 
#    d['c']=add(d['c'], "cd", "45") 
# else :
#    d['c'] = {"cd" : "45"}

# c= "kfc"
# for i in d.keys():
#    if i == c :
#       d[c]=add(d[c], "cd", "45")
#    if i!=c:
#       d[c]={"cd" : "45"}
# print(d)

# d["kfc"]=add(d["kfc"], "c", "45")
# c="ab"
# a=[]
# print(d)
# print()
# for i in d.keys():
#    a.append(i)
# if c  not in a:
#    d[c]={}
# print(a)
# print(d)

# print()
# d["ab"]=add(d["ab"], "c", "45")
# print(d)


# class my_dictionary(dict): 
#     # __init__ function 
#     def __init__(self): 
#         self = dict()   
#     # Function to add key:value 
#     def add(self, key, value): 
#         self[key] = value 
# # Main Function 
# dict_obj = my_dictionary() 
# limit = int(input("Enter the no of key value pair in a dictionary"))
# c=0
# while c < limit :   
#     dict_obj.key = input("Enter the key: ") 
#     dict_obj.value = input("Enter the value: ") 
#     dict_obj.add(dict_obj.key, dict_obj.value) 
#     c += 1
# print(dict_obj) 



# case_list = {"a" :{"name":"ab", "price":"20"}} 
# for entry in entries_list:
#     if key in case_list:
#         case_list[key1].append(value)
#     else:
#         case_list[key1] = [value] 


def add_food(d, key, value, isa):
    d[key] = {"price": value, "isAvailable": isa}
    return d

  


d={
  "chef":[
  {"name":"kfc",
    "items":
    [ 
      {"pizza": {"price": "400","isAvailable" : True,}}
    ]
    },

  {"name":"trail",
    "items":
    [ 
      {"pizza": {"price": "78","isAvailable" : True,}}
    ]
  }
  ]
}





# c="kfc"
# a = "burger"
# p = "500" 
# isA = True 
# ab=[] 
# dic=[{a:{"price": "500", "isAvailable": True}}]
# for i in d.keys():
#   ab.append(i) 

# if c in ab:
#   d.append(dict)

print(d)









# {
#   "success": {
#     "total": 1
#   },
#   "contents": {
#     "jokes": [
#       {
#         "category": "jod",
#         "title": "Joke of the day ",
#         "description": "Joke of the day ",
#         "background": "",
#         "date": "2019-01-23",
#         "joke": {
#           "title": "Courtship Signals",
#           "length": "83",
#           "clean": "1",
#           "racial": "0",
#           "date": "2019-01-23",
#           "id": "He3_WpaNfBV1Hs7zMLsR4QeF",
#           "text": "Q. Why shouldn't you marry a tennis player?\nA. Because he's a tennis player."
#         }
#       }
#     ] <-- this is the list of jokes
#   }