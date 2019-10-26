from fastapi import APIRouter

from climbing_grade_converter.db.database import (
    get_grades_from_style_with_type,
    get_grades_from_style,
    convert_grade,
)
from climbing_grade_converter.models.boulder import (
    BoulderGradeType,
    GradeConversionRequest,
    GradeConversionResponse,
)


router = APIRouter()

climbing_style = "boulder"


@router.get("/")
def read_boulder_grades():
    return get_grades_from_style(climbing_style)


@router.get("/{boulder_type}")
def read_type_grades(boulder_type: BoulderGradeType):
    return get_grades_from_style_with_type(climbing_style, boulder_type)


@router.post("/", response_model=GradeConversionResponse)
def create_convert_grade(request: GradeConversionRequest):
    return convert_grade(
        climbing_style, request.from_type, request.to_type, request.grade
    )
