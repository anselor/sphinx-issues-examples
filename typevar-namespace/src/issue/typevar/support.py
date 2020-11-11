from typing import (
    Generic,
    NewType,
    Optional,
    TypeVar,
)

#: This TypeVar declaration doesn't get resolved when generating docs
SharedTypeVar = TypeVar('SharedTypeVar')

#: NewType doesn't resolve correctly either
SpecialInt = NewType('SpecialInt', int)


class MyClass(Generic[SharedTypeVar]):
    def __init__(self, value: Optional[SharedTypeVar]):
        self._value = value
        self._special = SpecialInt(6)

    def value(self) -> SharedTypeVar:
        return self._value

    # This results in the following error:
    # docstring of issue.typevar.support.MyClass.special::py:class reference target not found: NewType.<locals>.new_type
    def special(self) -> SpecialInt:
        return self._special
