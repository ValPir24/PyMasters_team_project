from datetime import datetime

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


class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class CommentUpdate(CommentBase):
    pass

class CommentInDBBase(CommentBase):
    id: int
    user_id: int
    photo_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Comment(CommentInDBBase):
    pass

class TokenData(BaseModel):
    username: Optional[str] = None
    
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
