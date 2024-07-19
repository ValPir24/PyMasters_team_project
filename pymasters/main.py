from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routes.users import router as users_router


app = FastAPI()


app.include_router(users_router, prefix='/api')


@app.get("/")
def read_root():
    """
    Root endpoint to test API availability.
    """
    return {"message": "Hello World"}