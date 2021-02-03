from typing import (
    Any,
    Dict,
    Mapping,
    NewType,
)


# MyType = NewType('MyType', int)

class MyData(Dict[str, Any]):
    def __init__(self, value: Mapping[str, Any], blah: int) -> None:
        super(MyData, self).__init__(value)
        self._blah = blah

    @property
    def blah(self) -> int:
        return self._blah
