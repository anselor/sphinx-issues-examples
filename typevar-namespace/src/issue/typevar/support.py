from typing import (
    NewType,
)
from ._support_part1 import (
    SpecialString,
)
from ._support_part2 import (
    ImportedParentGeneric,
    MyTypeVar,
)

#: Custom string type
CustomString = NewType('CustomString', str)

# Adding this line appears to fix it for modules in the same package
CustomString.__qualname__ = f'{__name__}.CustomString'


__all__ = [
    'SpecialString',
    'CustomString',
    'MyTypeVar',
    'ImportedParentGeneric',
]
