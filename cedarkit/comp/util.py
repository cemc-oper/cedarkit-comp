from typing import Callable

import xarray as xr


def apply_to_xarray_values(field: xr.DataArray, func: Callable) -> xr.DataArray:
    input_values = field.values
    output_values = func(input_values)
    output_field = field.copy()
    output_field.values = output_values
    return output_field
