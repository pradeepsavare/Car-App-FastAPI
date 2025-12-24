from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# importing pymongo for future database interactions
import pymongo


app = FastAPI()

# connecting with database using pymongo client
client = pymongo.MongoClient("mongodb+srv://pradeepsavare:Pradeep123@cluster0.c055kzn.mongodb.net/")
# selecting database
database = client["mydatabase"]
db = client["mycompany"]
# selecting collection
collection = database["mycar"]
coll = db["employee"]


# sample dictionary for future use
# dictionary = {"name": "Pradeep", "age": 24, "city": "Pune"}
# list_of_dict = [
#     {"name": "Alice", "age": 30, "city": "New York"},
#     {"name": "Bob", "age": 25, "city": "Los Angeles"},
#     {"name": "Charlie", "age": 35, "city": "Chicago"}
# ]
# Below line is for testing purpose only for CRUD operations
# inserting sample dictionary into collection for creation
# coll.insert_one(dictionary)
# coll.insert_many(list_of_dict)
# retrieving one document from collection for reading
# data = coll.find_one()
# print(data)
# {'_id': ObjectId('694b9b71aea33fda201c8fa6'), 'name': 'Pradeep', 'age': 24, 'city': 'Pune'}
# data = coll.find_one({"name": "Alice"})
# data = coll.find({"name": "Alice"})
# print(data)
# retrieving multiple documents from collection for reading
# data_list = coll.find()
# print(list(data_list))

# or
# this will also work
# for i in data_list:
#     print(i)
# below give specific fields from the document
# cars = car_collection.find(
#     {},
#     {"carname": 1, "cardesc": 1, "_id": 0}
# )

# {
#   "carname": "Tesla Model S",
#   "cardesc": "Electric luxury sedan"
# }
# then updating document in collection for updating where name is Alice set age to 31
# data = coll.update_one({"name": "Alice"}, {"$set": {"age": 31}})
# print(data.modified_count)

# coll.delete_one({"name": "Bob"})
# deleting document from collection for deletion where name is Bob
# data = coll.delete_many({"name": "Bob"})

# various query operators examples
# this is greater than operator
# coll.find({"age": {"$gt": 25}})
# less than operator
# coll.find({"age": {"$lt": 30}})
# greater than equal to operator
# coll.find({"age": {"$gte": 30}})
# less than equal to operator
# coll.find({"age": {"$lte": 25}})
# not equal to operator
# coll.find({"age": {"$ne": 30}})
# in operator give ages 24 and 30
# coll.find({"age": {"$in": [24, 30]}})
# not in operator give ages except 25 and 35
# coll.find({"age": {"$nin": [25, 35]}})
# and operator give age greater than 25 and city Chicago
# coll.find({"$and": [{"age": {"$gt": 25}}, {"city": "Chicago"}]})
# or operator give age 24 or city New York
# coll.find({"$or": [{"age": 24}, {"city": "New York"}]})
# ascending sort give ages in ascending order
# coll.find().sort("age", pymongo.ASCENDING)
# descending sort give ages in descending order
# coll.find().sort("age", pymongo.DESCENDING)

# mounting static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# setting up Jinja2 templates
template = Jinja2Templates(directory="templates")

# defining home route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    collection.insert_one({"name": "Sample Car", "model": "2024"})
    return template.TemplateResponse(name = "home.html", request= request)

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    user= []
    row_data = coll.find()
    for i in row_data:
        print(i)
        user.append(i)
    print("User Data:")
    print(user)
    return template.TemplateResponse(name = "about.html", request= request, context={"user": user})

# this is updated home route to pass user data to template
# @app.get("/", response_class=HTMLResponse)
# def home(request: Request):
#     user = {
#         "name": "Pradeep",
#         "age": 24,
#         "city": "Pune"
#     }
#     return template.TemplateResponse("home.html", {"request": request}, context={"user": user})


# defining dynamic route to insert car details
# @app.get("/{name,model}", response_class=HTMLResponse)
# def home(request: Request,name,model):
#     collection.insert_one({"name": name, "model": model})
#     return template.TemplateResponse("home.html", {"request": request})