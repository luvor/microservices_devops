from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: Optional[int] = None
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    created: str = ""
    status: str = "new"
