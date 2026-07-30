import os  # pathlib.Path.walk not available in Python <3.12
import matplotlib.pyplot as plt
import thesistools
from .styles_discovery import read_styles_in_folders, update_nested_dict



# register the bundled stylesheets in the matplotlib style library
thesistools_path = thesistools.__path__[0]
styles_path = os.path.join(thesistools_path, "styles")



# Reads styles in /styles folder and all subfolders
stylesheets = read_styles_in_folders(styles_path)

# Update dictionary of styles - plt.style.library
update_nested_dict(plt.style.library, stylesheets)
# Update `plt.style.available`, mirroring matplotlib's own reload_library():
# https://github.com/matplotlib/matplotlib/blob/main/lib/matplotlib/style/__init__.py
plt.style.available[:] = sorted(
    name for name in plt.style.library if not name.startswith("_")
)

from .plotting import *
