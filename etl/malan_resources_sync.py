import pandas as pd

from app.django_orm import utils
from app.django_orm.content.models import MALANRawResource

utils.ensure_django()

GOOGLE_SHEET_ID = "1KMk34XY5dsvVJjAoD2mQUVHYU_Ib6COz6jcGH5uJWDY"

def malan_resources_sync():

    MALANRawResource.objects.all().delete()

    df = pd.read_csv(
        f"https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}/export?format=csv&id={GOOGLE_SHEET_ID}&gid=0", skiprows=2
        )

    df.columns = [column.strip() for column in df.columns]
    df = df.dropna(how='all')
    df = df[df['Closed']!=1.0]

    resources = []
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

        resources.append(res)

    MALANRawResource.objects.bulk_create(resources)


if __name__ == "__main__":
    malan_resources_sync()

