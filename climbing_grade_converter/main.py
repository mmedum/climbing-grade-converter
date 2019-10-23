from fastapi import FastAPI

from climbing_grade_converter.api.api_v1.api import router as api_router

app = FastAPI(title="Climbing Grade Converter")

app.include_router(api_router)
