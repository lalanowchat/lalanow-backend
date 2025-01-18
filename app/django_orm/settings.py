import environ
import os

env = environ.Env(DEBUG=(bool, False))

from dotenv import load_dotenv

load_dotenv()

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_TZ = True

DATABASES = {"default": env.db()}

# see: https://docs.djangoproject.com/en/4.2/ref/databases/#connection-management
CONN_HEALTH_CHECKS = True
CONN_MAX_AGE = 20  # I believe the default Postgres timeout is 30 seconds
INSTALLED_APPS = ["app.django_orm.content.config.DjangoConfig", 'django_extensions']

# if os.name == 'nt':
#     import platform
#     OSGEO4W = r"C:\OSGeo4W"
#     if '64' in platform.architecture()[0]:
#         OSGEO4W += "64"
#     assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
#     os.environ['OSGEO4W_ROOT'] = OSGEO4W
#     os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
#     os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
#     os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']