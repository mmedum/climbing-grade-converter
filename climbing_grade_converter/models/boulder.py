from enum import Enum
from pydantic import BaseModel
from typing import Dict
from typing import List


class BoulderGradeType(str, Enum):
    usa = "usa"
    french = "french"


class GradeConversionWithToTypeRequest(BaseModel):
    from_type: BoulderGradeType
    to_type: BoulderGradeType
    grade: str


class GradeConversionWithToTypeResponse(BaseModel):
    grade_type: BoulderGradeType
    grades: List


class GradeConversionNoToTypeRequest(BaseModel):
    grade: str


class GradeConversionNoToTypeResponse(BaseModel):
    grades: Dict[BoulderGradeType, List]
