from fastapi import APIRouter, Request
from starlette import status

from app.schemas.resources import (
    ResourcesListResponseSchema
)

router = APIRouter(prefix="/resources", tags=["resources"])


@router.get(
    "/list",
    response_model=ResourcesListResponseSchema,
)
def resources_list(request: Request):
    return {
        "resources": [
            {
                "name": "Lanark Recreation Center",
                "address": "21816 Lanark St, Canoga Park, CA 91304, USA"
            }
        ]
    }



