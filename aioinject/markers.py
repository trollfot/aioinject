import dataclasses
from typing import Any


@dataclasses.dataclass
class Inject:
    impl: Any = None
    cache: bool = True
