import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

from app.django_orm import utils
from app.django_orm.content.models import MALANRawResource, NeedHelpResource
from app.constants import NEED_HELP_CATEGORIES

utils.ensure_django()

GOOGLE_SHEET_ID = "1KMk34XY5dsvVJjAoD2mQUVHYU_Ib6COz6jcGH5uJWDY"

def get_coordinates(address):
    try:
        geolocator = Nominatim(user_agent="lalachatresponder@gmail.com")
        location = geolocator.geocode(address)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            return None, None
    except (GeocoderTimedOut, Exception):
        # If geocoding fails, continue without coordinates
        return None, None

def malan_resources_sync():

    MALANRawResource.objects.all().delete()
    NeedHelpResource.objects.all().delete()

    df = pd.read_csv(
        f"https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}/export?format=csv&id={GOOGLE_SHEET_ID}&gid=0", skiprows=2
        )

    df.columns = [column.strip() for column in df.columns]
    df = df.dropna(how='all')
    df = df[df['Closed']!=1.0]


    for i, row in df.iterrows():
        res = MALANRawResource(
                location=row.get('Location'),
                last_updated=row.get('Last Updated'),
                name=row.get('Name'),
                aid_type=row.get('Aid Type'),
                address=row.get('Address'),
                animals=row.get('Animals?'),
                volunteers_needs=row.get('Volunteers Needs'),
                accepting=row.get('Accepting'),
                providing=row.get('Providing'),
                notes=row.get('Notes'),
                source=row.get('Source'),
                closed=(True if row.get('Closed', False) == 1.0 else False),
                link=row.get('LINK (DO NOT HYPERLINK)'),
        )
        if (row.get('Address'), str) and isinstance(row.get('Aid Type'), str):
            latitude, longitude = get_coordinates(row.get('Address'))
            categories = row.get('Aid Type',"").split(",")
            for category in categories: 
                category = category.strip()
                if category in NEED_HELP_CATEGORIES:
                    nh_resource = NeedHelpResource(
                        name=res.name,
                        address=res.address,
                        providing=res.providing,
                        lat=latitude,
                        long=longitude,
                        aid_type=category,
                        last_updated=res.last_updated,
                    )
                    nh_resource.save()
            time.sleep(1)
        res.save()


if __name__ == "__main__":
    malan_resources_sync()

