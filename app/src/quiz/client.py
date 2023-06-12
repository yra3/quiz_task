from typing import List

import requests
from fastapi import HTTPException, status


def get_questions(count: int) -> List | Exception:
    response = requests.get('https://jservice.io/api/random', params={'count': count})
    if response.status_code != 200:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            'NotAvailable. Contact the server administrator.',
        )
    return response.json()
