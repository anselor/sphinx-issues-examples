from typing import (
    Generic,
    TypeVar,
)

from .support import (
    SharedTypeVar,  # imported TypeVar doesn't resolve correctly in Sphinx
)

#: Locally declared and referenced TypeVar appears to work fine
LocalTypeVar = TypeVar('LocalTypeVar')


class Successful(Generic[LocalTypeVar]):
    def __init__(self, arg: LocalTypeVar):
        self._value = arg

    def get_arg(self) -> LocalTypeVar:
        return self._value


class Fails(Generic[SharedTypeVar]):
    def __init__(self, arg: SharedTypeVar):
        self._value = arg

    def get_arg(self) -> SharedTypeVar:
        return self._value

