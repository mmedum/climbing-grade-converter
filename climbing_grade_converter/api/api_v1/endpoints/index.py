from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["index"])
def hello():
    return {"msg": "Hello from the Climbing Grade Converter!"}
