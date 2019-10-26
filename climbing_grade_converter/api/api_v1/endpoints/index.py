from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["index"])
def hello():
    return "Hello from the Climbing Grade Converter!"
