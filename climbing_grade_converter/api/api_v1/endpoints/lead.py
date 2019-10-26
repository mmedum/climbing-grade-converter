from fastapi import APIRouter

from climbing_grade_converter.db.database import (
    get_grades_from_style_with_type,
    get_grades_from_style,
    convert_grade,
)
from climbing_grade_converter.models.lead import (
    LeadGradeType,
    GradeConversionRequest,
    GradeConversionResponse,
)


router = APIRouter()

climbing_style = "lead"


@router.get("/")
def get_lead_grades():
    return get_grades_from_style(climbing_style)


@router.get("/{lead_type}")
def get_lead_type_grades(lead_type: LeadGradeType):
    return get_grades_from_style_with_type(climbing_style, lead_type)


@router.post("/", response_model=GradeConversionResponse)
def convert_lead_grade(request: GradeConversionRequest):
    return convert_grade(
        climbing_style, request.from_type, request.to_type, request.grade
    )
