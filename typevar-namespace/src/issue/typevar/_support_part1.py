from typing import NewType

#: Special string fails
SpecialString = NewType('SpecialString', str)

# Adding this line appears to fix it for modules in the same package
# SpecialString.__qualname__ = f'{__name__}.SpecialString'
