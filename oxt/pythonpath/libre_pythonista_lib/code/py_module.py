from __future__ import annotations
from typing import Any
import types


class PyModule:

    def __init__(self):

        self.mod = types.ModuleType("PyMod")
        self._init_mod()

    def _init_mod(self) -> None:
        code = """from __future__ import annotations
from typing import Any, cast
from ooodev.calc import CalcDoc
from ooodev.calc import CalcSheet
from ooodev.utils.data_type.cell_obj import CellObj
from ooodev.utils.data_type.range_obj import RangeObj
    """
        exec(code, self.mod.__dict__)
        self._init_dict = self.mod.__dict__.copy()
        # setattr(self.mod, "np", np)
        # setattr(self.mod, "Lo", lo)
        # setattr(self.mod, "XSCRIPTCONTEXT", Lo.XSCRIPTCONTEXT)
        # setattr(self.mod, "CalcDoc", CalcDoc)

    def reset_module(self):
        self.mod.__dict__.clear()
        self.mod.__dict__.update(self._init_dict)

    def update_with_result(self, code: str = "") -> Any:
        """
        Appends code to current module and returns the last variable in the module.

        Args:
            code (str, optional): Any valid python code

        Returns:
            Any: The last variable in the module if any; Otherwise, None.
        """
        if code:
            exec(code, self.mod.__dict__)
        # last_key = list(module.__dict__.keys())[-1]
        last_key = next(reversed(self.mod.__dict__), None)
        if last_key is None:
            return None
        result = getattr(self.mod, last_key)
        if callable(result):
            return None
        return result

    def reset_to_dict(self, mod_dict: dict, code: str = "") -> Any:
        """
        Reset the module to the given dictionary and returns the last variable in the module.

        Args:
            mod_dict (dict): A dictionary of variables to reset the module to.
            code (str, optional): Any valid python code

        Returns:
            Any: The last variable in the module if any; Otherwise, None.
        """
        self.mod.__dict__.clear()
        self.mod.__dict__.update(mod_dict)
        if code:
            exec(code, self.mod.__dict__)
        last_key = next(reversed(self.mod.__dict__), None)
        if last_key is None:
            return None
        result = getattr(self.mod, last_key)
        if callable(result):
            return None
        return result
