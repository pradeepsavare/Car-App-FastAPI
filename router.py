from fastapi import APIRouter

a = APIRouter()

@a.get("/")
def home():
    return {"hello" : "This is home"}

@a.get("/about")
def about():
    return {"hello" : "This is about"}