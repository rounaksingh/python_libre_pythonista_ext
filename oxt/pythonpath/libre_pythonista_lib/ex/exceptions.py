from __future__ import annotations
from typing import Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    from ooodev.utils.type_var import PathOrStr
    from ooodev.events.args.event_args_t import EventArgsT


class CustomPropertyError(Exception):
    """Custom Property Error."""

    pass


class CustomPropertyMissingError(CustomPropertyError):
    """Custom Property Missing Error."""

    pass


class CellDeletedError(Exception):
    """Cell Deleted Error."""

    pass
