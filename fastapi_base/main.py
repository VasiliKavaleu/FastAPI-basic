from fastapi import FastAPI, Query, Path, Body

# Query - для валидации параметров строки запроса /items?q=
# Path - валидация параметров url /items/{pk}
# Body - изменение параметров тела запросов

import uvicorn

from schemas import Book, Author


app = FastAPI()


@app.get('/')
def home():
    return {"key": "hello"}


@app.get('/user/{pk}') # добавление в параметры url параметр pk
def get_item(pk: int, q: str =None): # параметры функции не переданные в декоратор попадают в параметры строки запроса q: /5?q=value, если value в строке не указано, по умолчанию None
    return {"key": pk, "q": q}


@app.get('/user/{pk}/items/{item}') # возможны любые комбинации путей
def get_user_item(pk: int, item: str): 
    return {"user": pk, "item": item}


@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)): # передаваемые данные должны соответствовать модели Book, Author | для того чтобы параметр строки запроса перебросить в тело запроса исп Body
    return {"item": item, "author": author, "quantity": quantity}

"""
{
  "item": {
    "title": "string",
    "writer": "string",
    "duration": "string",
    "date": "2021-06-03",
    "summary": "string",
    "genres": [
      {
        "name": "string"
      }
    ],
    "pages": 0
  },
  "author": {
    "first_name": "string",
    "last_name": "string",
    "age": 0
  },
  "quantity": 0
}
"""


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)): # Body используем для Author с целью формирования доболнительной вложенности перед объектом с полями Author
    """
    Было:
        {
        "first_name": "string",
        "last_name": "string",
        "age": 0
        }

    Стало:
    {
    "author": {
        "first_name": "string",
        "last_name": "string",
        "age": 0
        }
    }
    """
    return {'author': author}


@app.get('/book')
def get_book(q: str = Query(None, min_length=2, max_length=5, description="Se arch books")): # Query позволет указвать мин и мак значения длины для данных которые мы хотим передать, 
    return q #  дефолтное значение, то вместо None указываем "this is default", для передачи списка значений оборачиваем str в List(str), /books?q=value1&q=value2 


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)): # валидация параметров url (Path)
    return {"pk": pk, "pages": pages}


@app.post('/new_book', response_model=Book, response_model_exclude_unset=True) # response_model_exclude_unset
def creat_book(item: Book):
    return item


if __name__ == '__main__':
    uvicorn.run("main:app", 
                port=80, 
                host="0.0.0.0", 
                reload=True)
