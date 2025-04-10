from functools import wraps
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def http_exception_wrapper(status_code=400):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except ValueError as e:
                raise HTTPException(status_code=status_code, detail=str(e))
            except IntegrityError as e:
                raise HTTPException(
                    status_code=400,
                    detail="Переданные данные не проходят валидацию или обьект уже создан"
                )
        return wrapper
    return decorator
