from fastapi import APIRouter

from climbing_grade_converter.db.database import (
    get_grades_from_style_with_type,
    get_grades_from_style,
)
from climbing_grade_converter.models.lead import LeadGradeType


router = APIRouter()

climbing_style = "lead"


@router.get("/")
def read_lead_grades():
    return get_grades_from_style(climbing_style)


@router.get("/{lead_type}")
def read_type_grades(lead_type: LeadGradeType):
    return get_grades_from_style_with_type(climbing_style, lead_type)
