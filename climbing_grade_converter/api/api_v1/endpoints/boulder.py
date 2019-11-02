from fastapi import APIRouter

from climbing_grade_converter.db.database import (
    get_grades_from_style_with_type,
    get_grades_from_style,
    convert_grade,
    convert_grades,
)
from climbing_grade_converter.models.boulder import (
    BoulderGradeType,
    GradeConversionWithToTypeRequest,
    GradeConversionWithToTypeResponse,
    GradeConversionNoToTypeRequest,
    GradeConversionNoToTypeResponse,
)


router = APIRouter()

climbing_style = "boulder"


@router.get("/")
def get_boulder_grades():
    return get_grades_from_style(climbing_style)


@router.get("/{boulder_type}")
def get_boulder_type_grades(boulder_type: BoulderGradeType):
    return get_grades_from_style_with_type(climbing_style, boulder_type)


@router.post("/{boulder_type}", response_model=GradeConversionNoToTypeResponse)
def convert_boulder_grades(
    boulder_type: BoulderGradeType, request: GradeConversionNoToTypeRequest
):
    return convert_grades(climbing_style, boulder_type, request.grade_type)


@router.post("/", response_model=GradeConversionWithToTypeResponse)
def convert_boulder_grade(request: GradeConversionWithToTypeRequest):
    return convert_grade(
        climbing_style, request.from_type, request.to_type, request.grade
    )
