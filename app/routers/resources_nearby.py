from fastapi import APIRouter, Request
from starlette import status

from app.schemas.resources_nearby import (
    ResourcesNearbyResponseSchema
)

router = APIRouter(prefix="/resources-nearby", tags=["resources-nearby"])


@router.get(
    "/list",
    response_model=ResourcesNearbyResponseSchema,
)
def resources_nearby(request: Request):
    return {
        "resources": [
            {
                "name": "Lanark Recreation Center",
                "address": "21816 Lanark St, Canoga Park, CA 91304, USA"
            }
        ]
    }



