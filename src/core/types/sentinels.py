class Empty:
    """A sentinel class used as placeholder."""

    def __str__(self) -> str:
        return "Empty"

    def __repr__(self) -> str:
        return "Empty"


class Undefined:
    """Sentinel class used to declare that the value is `Undefined`"""

    def __str__(self) -> str:
        return "Undefined"

    def __repr__(self) -> str:
        return "Undefined"


class Default:
    """Sentinel type used as a default type."""

    def __str__(self) -> str:
        return "Default"

    def __repr__(self) -> str:
        return "Default"


EmptyType = Empty
UndefinedType = Undefined
DefaultType = Default
