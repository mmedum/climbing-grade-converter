from enum import Enum
from pydantic import BaseModel


class BoulderGradeType(str, Enum):
    usa = "usa"
    french = "french"


class GradeConversionRequest(BaseModel):
    from_type: BoulderGradeType
    to_type: BoulderGradeType
    grade: str


class GradeConversionResponse(BaseModel):
    grade_type: BoulderGradeType
    grades: list
