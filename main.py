from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app= FastAPI()

@app.get('/')
async def read_root():
    return {
        "message": "fast api server is ready"
    }


# path parameters
@app.get('/greet/{name}')
async def greet_name(name:str) -> dict:
    return {
        "message": f"hello {name}"
    }

# for handling http request use restfox


@app.get('/greetings/{name}')
async def greet_name(name:str, age:int) -> dict:
    return {
        "message": f"hello {name}",
        "age": age
    }


# optional parameters with default values
# api= http://127.0.0.1:8000/greets?name=anis&age=20
# api= http://127.0.0.1:8000/greets
@app.get('/greets')
async def greet_name(name:Optional[str]="User", age:int=0) -> dict:
    return {
        "message": f"hello {name}",
        "age": age
    }


# request data post method
class BookCreate(BaseModel):
    title: str
    author: str
    year: int

@app.post('/create_book')
async def create_book(book: BookCreate) -> dict:
    return {
        "message": "book created",
        "title": book.title,
        "author": book.author,
        "year": book.year
    }