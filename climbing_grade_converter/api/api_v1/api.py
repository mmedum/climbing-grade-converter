from fastapi import APIRouter

from .endpoints.index import router as index_router
from .endpoints.boulder import router as boulder_router
from .endpoints.lead import router as lead_router


router = APIRouter()
router.include_router(index_router, tags=["index"])
router.include_router(boulder_router, prefix="/boulder", tags=["boulder"])
router.include_router(lead_router, prefix="/lead", tags=["lead"])
