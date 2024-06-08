from __future__ import annotations
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ....___lo_pip___.lo_util.resource_resolver import ResourceResolver
else:
    from ___lo_pip___.lo_util.resource_resolver import ResourceResolver


class ResResolver(ResourceResolver):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ResResolver, cls).__new__(cls, *args, **kwargs)
            cls._instance._is_init = False
        return cls._instance

    def __init__(self):
        if getattr(self, "_is_init", False):
            return
        from ooodev.loader import Lo

        ctx = Lo.get_context()
        super().__init__(ctx)
        self._is_init = True
