from typing import Optional, Any
from .interactions import Interaction

class Command:
    interaction: Interaction

class Option:
    description: Optional[str]
    default: Any
