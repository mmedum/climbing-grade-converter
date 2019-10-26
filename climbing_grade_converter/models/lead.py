from enum import Enum
from pydantic import BaseModel


class LeadGradeType(str, Enum):
    usa = "usa"
    french = "french"
    australia = "australia"
    uiaa = "uiaa"
    southafrica = "southafrica"
    uk = "uk"


class GradeConversionModel(BaseModel):
    from_type: LeadGradeType
    to_type: LeadGradeType
    grade: str
