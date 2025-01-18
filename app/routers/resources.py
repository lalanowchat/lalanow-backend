from fastapi import APIRouter, Request, Query, HTTPException
from starlette import status
from typing import List, Optional
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

from app.schemas.resources import (
    ResourcesListResponseSchema
)
from app.django_orm.content.models import MALANRawResource, NeedHelpResource
from app.django_orm.content.db_utils import execute_custom_query
from app.constants import NEED_HELP_CATEGORIES


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
    categories = NEED_HELP_CATEGORIES

    return categories

@router.get(
    "/need-help",  # Added trailing slash
    status_code=status.HTTP_200_OK,
)
def need_help(
    request: Request,
    category: str = Query(..., description="Category of help needed"),
    location: Optional[str] = Query(default=None, description="Location to search for resources"),
):

    if location is None or location == "":
        resources = MALANRawResource.objects.filter(
            aid_type=category,
        ).values('name', 'address', 'providing')
    else:
        resources = MALANRawResource.objects.filter(
            aid_type=category,
            location=location
        ).values('name', 'address', 'providing')

    return {
        "resources": list(resources)
    }

@router.get(
    "/need-help/by-zip",
    status_code=status.HTTP_200_OK,
)
def need_help_by_zip(
    request: Request,
    category: str = Query(..., description="Category of help needed"),
    zipcode: str = Query(..., description="ZIP code to search near"),
):
    # Get coordinates for the ZIP code
    geolocator = Nominatim(user_agent="lalachatresponder@gmail.com")
    try:
        location = geolocator.geocode(f"{zipcode}, USA")
        if not location:
            raise HTTPException(
                status_code=404,
                detail=f"Could not find coordinates for ZIP code {zipcode}"
            )
        search_lat = location.latitude
        search_long = location.longitude
    except GeocoderTimedOut:
        raise HTTPException(
            status_code=503,
            detail="Geocoding service timed out"
        )

    # Create raw SQL query using PostGIS

    query = f"""
        SELECT 
            name,
            aid_type,
            address,
            providing,
            (
                3959 * acos(
                    cos(radians({search_lat})) * 
                    cos(radians(lat)) * 
                    cos(radians(long) - radians({search_long})) + 
                    sin(radians({search_lat})) * 
                    sin(radians(lat))
                )
            ) AS distance
        FROM app_django_orm_needhelpresource
        WHERE 
            aid_type = '{category}'
            and address != 'nan'
            AND lat IS NOT NULL 
            AND long IS NOT NULL
        ORDER BY distance 
        LIMIT 10;
    """

    resources = execute_custom_query(query)    

    return {
        "resources": resources
    }

   
