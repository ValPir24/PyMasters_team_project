from datetime import date

from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr


class PhotoBase(BaseModel):
    
    photo_urls: str


class UserModel(BaseModel):
    username: str
    password: str


class EmailSchema(BaseModel):

    email: EmailStr


class RequestEmail(BaseModel):

    email: EmailStr


class UserDisplayModel(BaseModel):

    email: str
    avatar_urls: str
