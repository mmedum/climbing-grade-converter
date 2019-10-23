from pydantic import BaseModel


class GradeConversion(BaseModel):
    from_type: str
    to_type: str
    grade: str
