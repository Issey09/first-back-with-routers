from typing import Annotated

from pydantic import BaseModel


class User(BaseModel):
    nickname: str
