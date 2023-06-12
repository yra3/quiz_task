from typing import List, Tuple

from sqlalchemy import desc
from sqlalchemy.orm import Session, Query

from src.database import Question
from src.quiz import client as quiz_client


def get_last_question(db: Session) -> Question:
    return db.query(Question).order_by(desc(Question.created_at)).first()


def pull_questions(questions_to_pull: int, db: Session) -> None:
    while questions_to_pull:
        questions_json = quiz_client.get_questions(questions_to_pull)

        question_texts: Tuple = tuple([question['question'] for question in questions_json])
        repeated_questions:  Query = db.query(Question).filter(Question.text.in_(question_texts)).all()
        questions_to_pull = repeated_questions.count(Question.id)

        new_questions_json = exclude_old_questions(questions_json, repeated_questions)
        new_questions = [Question(text=question['question'], answer=question['answer'])
                         for question in new_questions_json]
        db.add_all(new_questions)
        db.commit()


def exclude_old_questions(questions_json: List, questions_to_exclude: Query) -> List:
    old_question_texts = [question.text for question in questions_to_exclude]
    questions = []
    for question in questions_json:
        if question['question'] not in old_question_texts:
            questions.append(question)
    return questions
