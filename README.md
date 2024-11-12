# cedarkit-comp

![GitHub Release](https://img.shields.io/github/v/release/cemc-oper/cedarkit-comp)
![PyPI - Version](https://img.shields.io/pypi/v/cedarkit-comp)
![GitHub License](https://img.shields.io/github/license/cemc-oper/cedarkit-comp)
![GitHub Action Workflow Status](https://github.com/cemc-oper/cedarkit-comp/actions/workflows/ci.yaml/badge.svg)

A calculation tool for meteorological data.

## Install

Install using pip:

```bash
pip install cedarkit-comp
```

Or download the latest source code from GitHub and install manually.

## Getting started

Load data from file:

```py
from reki.format.grib.eccode import load_field_from_file

file_path = "/some/path/to/grib2/file"
field_h_500 = load_field_from_file(
    file_path,
    parameter="gh",
    level_type="pl",
    level=500
) / 10.
```

Smooth using `smth9`:

```py
from cedarkit.comp.smooth import smth9
from cedarkit.comp.util import apply_to_xarray_values

field_h_500 = apply_to_xarray_values(
    field_h_500, 
    lambda x: smth9(x, 0.5, 0.25, False)
)
```

## LICENSE

Copyright &copy; 2024, developers at cemc-oper.

`cedarkit-comp` is licensed under [Apache License V2.0](./LICENSE)