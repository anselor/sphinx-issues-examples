from typing import Generic, TypeVar

#: my type variable
MyTypeVar = TypeVar('MyTypeVar')
# MyTypeVar.__qualname__ = f'{__name__}.MyTypeVar'

class ImportedParentGeneric(Generic[MyTypeVar]):

    def __init__(self, param: MyTypeVar) -> None:
        super().__init__()
        self._param: MyTypeVar = param
