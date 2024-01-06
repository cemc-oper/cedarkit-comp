import numpy as np
from scipy import signal


def smth9(x: np.ndarray, p: float, q: float, wrap: bool = False) -> np.ndarray:
    """
    NCL smth9 function.

    Parameters
    ----------
    x
    p
    q
    wrap

    Returns
    -------
    np.ndarray

    Notes
    ----------
    NCL smth9 documentation:

    This function performs 9-point smoothing using the equation:

    f0 = f0 + (p / 4) * (f2 + f4 + f6 + f8 - 4 * f0) + (q / 4) * (f1 + f3 + f5 + f7 - 4 * f0)

    where f0, f1 (and so on) are as indicated:
          1-------------8---------------7
          |             |               |
          |             |               |
          |             |               |
          |             |               |
          2-------------0---------------6
          |             |               |
          |             |               |
          |             |               |
          |             |               |
          3-------------4---------------5
    This function is primarily used prior to plotting for nicer looking plots.
    Missing values are allowed and are indicated by the _FillValue attribute (x@_FillValue).
    Use the smth9_Wrap function if metadata retention is desired. The interface is identical.

    References
    ----------
    https://www.ncl.ucar.edu/Document/Functions/Built-in/smth9.shtml

    https://www.pyngl.ucar.edu/Examples/Scripts/meteogram.py

    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html
    """
    kernel = np.array(
        [
            [q / 4., p / 4., q / 4.],
            [p / 4., 1 - p - q, p / 4.],
            [q / 4., p / 4., q / 4.],
        ]
    )

    if wrap:
        boundary = "wrap"
    else:
        boundary = "fill"

    output = signal.convolve2d(
        x, kernel,
        boundary=boundary,
        mode='same',
        fillvalue=0.
    )

    # TODO: when wrap is True, left and right column should not be replaced.
    output[0, :] = x[0, :]
    output[-1, :] = x[-1, :]
    output[:, 0] = x[:, 0]
    output[:, -1] = x[:, -1]

    return output
