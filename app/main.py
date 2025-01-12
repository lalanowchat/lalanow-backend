from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from importlib.metadata import version

from app.constants import IS_DEPLOYED
from app.dependencies import get_api_key
from app.routers import resources_nearby


load_dotenv(".env")

try:
    API_VERSION = version("lalanow-backend")
except:
    API_VERSION = "Unknown"

app = FastAPI(
    title="python_api_template",
    version=API_VERSION,
    dependencies=[Depends(get_api_key)] if IS_DEPLOYED else [],
    description="The Backend of LALA Now Chatbot",
)


app.include_router(resources_nearby.router)
