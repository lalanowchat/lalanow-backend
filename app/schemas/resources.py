from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class ResourceSchema(BaseModel):
    name: str
    address: Optional[str]

