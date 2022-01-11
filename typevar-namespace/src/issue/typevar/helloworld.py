from typing import (
    Generic,
    NewType,
    TypeVar,
)

from .support import (
    CustomString,
    SpecialString,
    ImportedParentGeneric,
    MyTypeVar,
)

#: my type variable
LocalTypeVar = TypeVar('LocalTypeVar')
# MyTypeVar.__qualname__ = f'{__name__}.MyTypeVar'

class ParentGeneric(Generic[LocalTypeVar]):

    def __init__(self, param: LocalTypeVar) -> None:
        super().__init__()
        self._param: LocalTypeVar = param


#: locally declared newtype resolves correctly
LocalCustomString = NewType('LocalCustomString', str)


class MySubclass(ParentGeneric[LocalCustomString]):
    """
    [summary]

    :param ParentGeneric: [description]
    :type ParentGeneric: [type]
    """
    Local: LocalCustomString = LocalCustomString('Local')
    Imported: CustomString = CustomString('Imported')
    Special: SpecialString = SpecialString('Special')


class MySubclass2(ImportedParentGeneric[SpecialString]):
    def __init__(self, param: SpecialString) -> None:
        super().__init__(param)
        