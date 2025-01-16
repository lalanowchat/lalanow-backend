from fastapi import APIRouter, Request, Query
from starlette import status
from typing import List

from app.schemas.resources import (
    ResourcesListResponseSchema
)

from app.django_orm.content.models import MALANRawResource

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


@router.get(
    "/locations",
    response_model=List[str],
    status_code=status.HTTP_200_OK,
)
def unique_locations(request: Request):
    # Get distinct location values, excluding None/null values
    locations = MALANRawResource.objects.exclude(
        location__isnull=True
    ).values_list('location', flat=True).distinct()
    
    return list(locations)


@router.get(
    "/need-help-categories",
    response_model=List[str],
    status_code=status.HTTP_200_OK,
)
def need_help_categories(request: Request):
    categories = [
        "Free Prepared Meals",
        "Wifi/Charging",
        "Animal Boarding",
        "Services",
        "Free Items"
    ]
    return categories

@router.get(
    "/need-help",  # Added trailing slash
    status_code=status.HTTP_200_OK,
)
def need_help(
    request: Request,
    category: str = Query(..., description="Category of help needed"),
    location: str = Query(..., description="Location to search for resources"),
):
    resources = MALANRawResource.objects.filter(
        aid_type=category,
        location=location
    ).values('name', 'address', 'providing')

    return {
        "resources": list(resources)
    }

