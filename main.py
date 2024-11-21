from fastapi import FastAPI, status
from typing import Optional, List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
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

# ----------------------------------------------------------

# use book json

books=[
  {
    "id": 1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publisher": "J.B. Lippincott & Co.",
    "published_date": "1960-07-11",
    "page_count": 281,
    "language": "English"
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "publisher": "Secker & Warburg",
    "published_date": "1949-06-08",
    "page_count": 328,
    "language": "English"
  },
  {
    "id": 3,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "publisher": "T. Egerton, Whitehall",
    "published_date": "1813-01-28",
    "page_count": 432,
    "language": "English"
  },
  {
    "id": 4,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publisher": "Charles Scribner's Sons",
    "published_date": "1925-04-10",
    "page_count": 218,
    "language": "English"
  },
  {
    "id": 5,
    "title": "Moby Dick",
    "author": "Herman Melville",
    "publisher": "Harper & Brothers",
    "published_date": "1851-11-14",
    "page_count": 635,
    "language": "English"
  },
  {
    "id": 6,
    "title": "War and Peace",
    "author": "Leo Tolstoy",
    "publisher": "The Russian Messenger",
    "published_date": "1869-01-01",
    "page_count": 1225,
    "language": "Russian"
  },
  {
    "id": 7,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "publisher": "Little, Brown and Company",
    "published_date": "1951-07-16",
    "page_count": 277,
    "language": "English"
  },
  {
    "id": 8,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "publisher": "George Allen & Unwin",
    "published_date": "1937-09-21",
    "page_count": 310,
    "language": "English"
  },
  {
    "id": 9,
    "title": "Crime and Punishment",
    "author": "Fyodor Dostoevsky",
    "publisher": "The Russian Messenger",
    "published_date": "1866-01-01",
    "page_count": 671,
    "language": "Russian"
  },
  {
    "id": 10,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "publisher": "HarperCollins",
    "published_date": "1988-01-01",
    "page_count": 208,
    "language": "Portuguese"
  }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int 
    language: str


class BookUpdateModel(BaseModel):
  title: str
  author: str
  publisher: str
  page_count: int 
  language: str



# get all books
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


# post a books
@app.post('/books', status_code= status.HTTP_201_CREATED)
async def post_a_book(book_data: Book)->dict:
    new_book= book_data.model_dump()
    books.append(new_book)
    return new_book

# get single book
@app.get("/books/{book_id}")
async def single_book(book_id:int) -> dict:
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="book not found"

    )


# update book
@app.patch("/books/{book_id}")
async def update_book(book_id:int, u_book: BookUpdateModel):
  for book in books:
    if book["id"]==book_id:
      book["title"]=u_book.title
      book["author"]=u_book.author
      book["publisher"]=u_book.publisher
      book["page_count"]=u_book.page_count
      book["language"]=u_book.language
      return book

# delete a book
@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int):
  for book in books:
    if book["id"]== book_id:
      books.remove(book)
      return {}
       
