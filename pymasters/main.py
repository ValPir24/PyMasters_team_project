from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# from routes.users import router as users_router
# from routes.photos import router as photos_router 
from pymasters.routes.users import router as users_router
from pymasters.routes.photos import router as photos_router

app = FastAPI()

app.include_router(users_router, prefix='/api')
app.include_router(photos_router, prefix='/api')  # Додаємо маршрутизатор для світлин

@app.get("/")
def read_root():
    """
    Root endpoint to test API availability.
    """
    return {"message": "Hello World"}
