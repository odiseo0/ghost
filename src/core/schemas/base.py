from enum import Enum, EnumMeta
from typing import TYPE_CHECKING, Any, Self, Iterator, Protocol

from pydantic import BaseModel as _BaseModel
from pydantic import ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.utils import ROOT_KEY

from ..utils import deserialize_object, serialize_object


if TYPE_CHECKING:
    from pydantic.typing import AbstractSetIntStr, MappingIntStrAny


class SupportsIter(Protocol):
    """Implement `__iter__` method."""

    def __iter__(self) -> Iterator:
        ...


class SupportsDict(Protocol):
    """Implement `__dict__` method."""

    def __dict__(self) -> dict[str, Any]:
        ...


class BaseModel(_BaseModel):
    """Base schema for all objects."""

    __slots__ = ()

    class Config:
        exclude = set()
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        json_loads = deserialize_object
        json_dumps = serialize_object
        json_encoders = {
            Enum: lambda enum: enum.value if enum else None,
            EnumMeta: None,
        }

    @classmethod
    def parse_obj(cls: Self, obj: SupportsIter | SupportsDict) -> Self:
        """Redefined to use `vars()` instead of `dict()`."""
        obj = cls._enforce_dict_if_root(obj)

        if not isinstance(obj, dict):
            try:
                obj = dict(obj)
            except Exception:
                try:
                    obj = vars(obj)
                except Exception as e:
                    exc = TypeError(
                        f"{cls.__name__} expected dict not {obj.__class__.__name__}"
                    )
                    raise ValidationError([ErrorWrapper(exc, loc=ROOT_KEY)], cls) from e

        return cls(**obj)

    def dict(
        self,
        *,
        include: "AbstractSetIntStr | MappingIntStrAny" = None,
        exclude: "AbstractSetIntStr | MappingIntStrAny" = None,
        by_alias: bool = False,
        skip_defaults: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ) -> dict[str, Any]:
        exclude = exclude or set()
        exclude = (
            exclude.union(getattr(self.Config, "exclude", set()))
            if not isinstance(exclude, dict)
            else exclude
        )

        if len(exclude) == 0:
            exclude = None

        return super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )
