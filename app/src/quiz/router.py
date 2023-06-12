from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.quiz import service
from src.quiz.service import pull_questions

router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK)
def get_question(
    questions_num: int = Query(ge=0, le=100),
    db: Session = Depends(get_db),
) -> JSONResponse:
    last_question = service.get_last_question(db)
    pull_questions(questions_num, db)
    content = {}
    if last_question:
        content = {
            'question_id': last_question.id,
            'question': last_question.text,
            'answer': last_question.answer,
            'date': last_question.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
        }
    return JSONResponse(content)
