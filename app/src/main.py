from fastapi import FastAPI

from src.quiz.router import router as quiz_router

app = FastAPI()

app.include_router(quiz_router, prefix="/quiz", tags=["Quiz"])
