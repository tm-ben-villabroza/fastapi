from typing import List
from pydantic import BaseModel


class HasPermissionRequest(BaseModel):
    permission_names: List[str]
