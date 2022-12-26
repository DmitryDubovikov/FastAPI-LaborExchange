import datetime
from pydantic import BaseModel


class BaseJob(BaseModel):
    title: str
    description: str
    is_active: bool = True

class Job(BaseJob):
    id: int
    user_id: int


class JobIn(BaseJob):
    pass
