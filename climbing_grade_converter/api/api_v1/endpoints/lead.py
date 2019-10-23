from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["lead"])
def convert_boulder_grade():
    return "Lead convert"
