from datetime import date

from typing import List, Optional
from fastapi import UploadFile

from pydantic import BaseModel, Field, EmailStr


class PhotoBase(BaseModel):
    photo_urls: str
    description: Optional[str] = None
    tags: List[str] = []  # Додано поле для тегів

class PhotoCreate(BaseModel):
    file: UploadFile
    description: Optional[str] = None
    tags: Optional[List[str]] = None

class PhotoUpdate(BaseModel):
    description: Optional[str] = None

class PhotoDisplay(BaseModel):
    id: int
    photo_urls: str
    description: Optional[str] = None
    tags: List[str] = []

    class Config:
        orm_mode = True


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
