from pydantic import BaseModel, validator, Field

from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description="Author age must be more then 15 and less then 90")

    # @validator('age') # в ковычках передаем поле которое необходимо валидировать
    # def check_age(cls, v): # v - значение которое будем проверять
    #     if v < 15:
    #         raise ValueError
    #     return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str = None # по умолчанию None
    genres: List[Genre] # список жанров (жанры в виде объектов), может быть пустым
    pages: int
