from typing import Any
from uuid import UUID

import orjson


def serialize_object(obj: Any) -> str:
    """Encodes a python object to a json string."""

    def _serialize(val: Any) -> Any:
        if isinstance(val, UUID):
            return str(val)

    return orjson.dumps(
        obj,
        default=_serialize,
        option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY,
    ).decode()


def deserialize_object(
    obj: bytes | bytearray | memoryview | str | dict[str, Any]
) -> Any:
    """Decodes an object to a python datatype."""
    if isinstance(obj, dict):
        return obj

    return orjson.loads(obj)
