from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["boulder"])
def convert_boulder_grade():
    return "Boulder convert"
