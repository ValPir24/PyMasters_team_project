from fastapi import FastAPI, Request, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

# from routes.users import router as users_router
# from routes.photos import router as photos_router 
from pymasters.routes.users import router as users_router
from pymasters.routes.photos import router as photos_router
from pymasters.schemas import CommentCreate, Comment, CommentUpdate
from pymasters.settings import get_current_user
from pymasters.database.db import get_db
from pymasters.database.models import User

app = FastAPI()

app.include_router(users_router, prefix='/api')
app.include_router(photos_router, prefix='/api')  # Додаємо маршрутизатор для світлин

@app.get("/")
def read_root():
    """
    Root endpoint to test API availability.
    """
    return {"message": "Hello World"}

@app.post("/photos/{photo_id}/comments/", response_model=Comment)
def create_comment(photo_id: int, comment: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_comment = Comment(**comment.dict(), photo_id=photo_id, user_id=current_user.id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@app.put("/comments/{comment_id}/", response_model=Comment)
def update_comment(comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if db_comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this comment")
    for key, value in comment.dict().items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@app.delete("/comments/{comment_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if current_user.role not in ['admin', 'moderator']:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")
    db.delete(db_comment)
    db.commit()
    return None
