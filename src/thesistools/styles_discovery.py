'''Based on https://github.com/garrettj403/SciencePlots/blob/master/scienceplots/styles_discovery.py

Reimplements the two helpers that used to be taken from ``matplotlib.style.core``
(``read_style_directory`` and ``update_nested_dict``). That module was deprecated
in matplotlib 3.10 and removed in 3.11, so only public API is used here:
``matplotlib.rc_params_from_file`` plus the ``matplotlib.style`` library/available
containers, which are a plain dict and a plain list in every version.
'''

import logging
import os
import warnings
from pathlib import Path

import matplotlib as mpl

STYLE_EXTENSION = "mplstyle"

_log = logging.getLogger(__name__)


def read_style_directory(style_dir):
    """
    Reads all stylesheets directly inside the given folder.

    Parameters
    ----------
    style_dir : str or pathlib.Path
        Folder to scan for ``*.mplstyle`` files (not recursive).

    Returns
    -------
    styles : dict
        Dictionary in the form of {style_name: rcParams}.
    """
    styles = {}
    for path in sorted(Path(style_dir).glob(f"*.{STYLE_EXTENSION}")):
        with warnings.catch_warnings(record=True) as warns:
            warnings.simplefilter("always")
            styles[path.stem] = mpl.rc_params_from_file(
                path, use_default_template=False
            )
        for warn in warns:
            _log.warning("In %s: %s", path, warn.message)
    return styles


def update_nested_dict(main_dict, new_dict):
    """
    Updates a dictionary of dictionaries, merging one level deep.

    Parameters
    ----------
    main_dict : dict
        Dictionary to update in place, e.g. ``plt.style.library``.
    new_dict : dict
        Dictionary of new values.

    Returns
    -------
    main_dict : dict
        The updated dictionary (same object that was passed in).
    """
    for name, rc_dict in new_dict.items():
        if isinstance(rc_dict, dict) and isinstance(main_dict.get(name), dict):
            main_dict[name].update(rc_dict)
        else:
            main_dict[name] = rc_dict
    return main_dict


def read_styles_in_folders(root_path):
    """
    Reads all stylesheets in the given path and its subfolders.

    Parameters
    ----------
    root_path : str
        Path to the root folder containing the stylesheets and other subfolders
        with stylesheets.

    Returns
    -------
    stylesheets : dict
        Dictionary of stylesheets in the form of {style_name: rcParams}.
        Should be compatible with matplotlib's plt.style.library dictionary.
    """
    stylesheets = {}  # plt.style.library is a dictionary
    for folder, _, _ in os.walk(root_path):
        new_stylesheets = read_style_directory(folder)
        stylesheets.update(new_stylesheets)
    return stylesheets
