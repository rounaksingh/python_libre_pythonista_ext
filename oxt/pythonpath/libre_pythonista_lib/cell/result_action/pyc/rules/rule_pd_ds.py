from __future__ import annotations
from typing import Any, cast
from collections import OrderedDict
from ooodev.calc import CalcCell
import pandas as pd
from .rule_base import RuleBase
from .....cell.state.ctl_state import CtlState
from .....cell.state.state_kind import StateKind
from .....const import UNO_DISPATCH_DS_STATE
from .....utils.pandas_util import PandasUtil


class RulePdDs(RuleBase):
    """Rule for handling pandas DataSeries."""

    def __init__(self, cell: CalcCell, data: Any) -> None:  # noqa: ANN401
        super().__init__(cell, data)
        self.state_key = self.key_maker.ctl_state_key

    def _get_data_type_name(self) -> str:
        return self.key_maker.rule_names.cell_data_type_pd_series

    def get_dispatch_state(self) -> str:
        """
        Gets the dispatch command from the const ``UNO_DISPATCH_DS_STATE``.
        """
        return UNO_DISPATCH_DS_STATE

    def get_is_match(self) -> bool:
        result = self.data.get("data", None)
        if result is None:
            return False
        return isinstance(result, pd.Series)

    def _get_state(self) -> StateKind:
        state = CtlState(self.cell).get_state()
        return state

    def _set_state(self, state: StateKind) -> None:
        CtlState(self.cell).set_state(state)

    def _pandas_to_array(self) -> Any:  # noqa: ANN401
        ds = cast(pd.Series, self.data.data)
        if PandasUtil.is_date_series(ds):
            ds_copy = ds.copy()
            PandasUtil.pandas_series_to_lo_calc(ds_copy)
            d = ds_copy.to_dict(into=OrderedDict)
        else:
            d = ds.to_dict(into=OrderedDict)

        d = PandasUtil.convert_dict_keys_to_lo_date(d)

        list_2d = [[k, v] for k, v in d.items()]
        if ds.name:
            list_2d.insert(0, ["", ds.name])
        return list_2d

    def action(self) -> Any:  # noqa: ANN401
        state = self._get_state()
        self._update_properties(
            **{
                self.key_maker.cell_array_ability_key: True,
                self.cell_prop_key: self.data_type_name,
                self.cell_pyc_rule_key: self.data_type_name,
                self.state_key: state,
            }
        )
        if state == StateKind.ARRAY:
            return self._pandas_to_array()
        return (("",),)

    def __repr__(self) -> str:
        return f"<RulePdDs({self.cell.cell_obj}, {type(self.data).__name__})>"
