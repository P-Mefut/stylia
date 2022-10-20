import matplotlib as mpl
import seaborn as sns
import shutil
import os

sns.set_style("ticks")

os.environ["LC_CTYPE"] = "en_US.UTF-8"
import matplotlib.font_manager

FONT = "Arial"

shutil.rmtree(mpl.get_cachedir())

mpl.rcParams["font.family"] = "sans-serif"
mpl.rcParams["font.sans-serif"] = FONT
mpl.rcParams.update({"font.size": 10})
mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
mpl.rcParams.update({"axes.grid": True})

# Relative imports

from .figure import create_figure, save_figure, figure_size_limits

from .colors.colors import NamedColors, NamedColorMaps, ContinuousColorMap
