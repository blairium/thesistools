import os  # pathlib.Path.walk not available in Python <3.12
import matplotlib.pyplot as plt


style = plt.style.core.read_style_directory(os.getcwd())


# Update dictionary of styles - plt.style.library
plt.style.core.update_nested_dict(plt.style.library, style)
# Update `plt.style.available`, copy-paste from:
# https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266  # noqa: E501
plt.style.core.available[:] = sorted(plt.style.library.keys())

from .plotting import *
