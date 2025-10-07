# thesistools/plotting.py
"""_summary_
A collection of plotting tools for the Latex Thesis template
Author: Blair Haydon 2025
"""

from __future__ import annotations
from string import ascii_lowercase
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from dataclasses import dataclass


@dataclass
class panel_labeller:
    """
    Class for generating sequential labels for plot panels.
    """

    sequence: str = ascii_lowercase
    _label_index: int = 0

    def next(self) -> str:
        """
        Get the next label in the sequence.
        Returns:
            str: The next label.
        """
        label = self.sequence[self._label_index]
        self._label_index += 1
        return label


def add_subfig_label(
    ax,
    label: str,
    facecolor: str = "0.7",
    edgecolor: str = "none",
    alpha: float = 0.5,
    align: str = "left",
    brackets: bool = True,
    *args,
    **kwargs,
):
    """
    Add a label to a subfigure.

    Parameters:
        ax (mpl.axes.Axes): The subplot axis to label.
        label (str): The label text.
        description (str, optional): Additional description text.
    """
    ax.set_ybound(upper=ax.get_ybound()[1] * 1.05)
    ax.annotate(
        f"({label})" if brackets else f"{label}",
        xy=(0 if align == "left" else 1, 1),
        xycoords="axes fraction",
        xytext=(+0.5 if align == "left" else -0.5, -0.5),
        horizontalalignment=align,
        textcoords="offset fontsize",
        fontsize="medium",
        verticalalignment="top",
        fontfamily="serif",
        bbox=dict(
            facecolor=facecolor,
            edgecolor=edgecolor,
            pad=3.0,
            alpha=alpha,
            *args,
            **kwargs,
        ),
    )


def set_size(aspect: float | str = "wide"):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float
            Document textwidth or columnwidth in pts
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    fig_width_pt: float = 438.17247  # pt
    inches_per_pt: float = 1 / 72.27
    golden_ratio: float = (5**0.5 - 1) / 2
    fig_width_in: float = fig_width_pt * inches_per_pt
    if aspect == "wide":
        fig_height_in: float = fig_width_in * golden_ratio
    elif aspect == "tall":
        fig_height_in: float = fig_width_in / golden_ratio
    elif type(aspect) in [float, int]:
        fig_height_in: float = fig_width_in * aspect
    else:
        fig_height_in: float = fig_width_in
    fig_dim: float = (fig_width_in, fig_height_in)

    return fig_dim


def get_colour(key):
    colour_dict = {
        "CPS": "k",
        "Rec": "#332288",
        "Bulk": "#DDCC77",
        "B*": "#882255",
        "Envelope": "#CC6677",
        "Background": "#DDDDDD",
        "CH": "#984ea3",
        "OH": "#999933",
        "Carbonyl": "#882255",
        "Ether": "#225522",
        "DB": "#BB5566",
        "Dimer": "#332288",
        "D2": "#6A5CB1",
        "Pandey Chain": "#332288",
    }
    if key in colour_dict:
        return colour_dict[key]
    else:
        return "#555555"


def offset(myFig, myAx, n=1, yOff=60):
    dx, dy = 0.0, yOff / myFig.dpi
    return myAx.transData + mpl.transforms.ScaledTranslation(
        dx, n * dy, myFig.dpi_scale_trans
    )


def presentation_size(
    size: str, SMALL_SIZE: int = 24, MEDIUM_SIZE: int = 32, BIGGER_SIZE: int = 40
):
    golden_mean = (np.sqrt(5) - 1.0) / 2.0  # Aesthetic ratio\n",

    widths = {
        "A0": 46.8,
        "A1": 33.1,
        "A2": 23.4,
        "A3": 16.5,
        "A4": 11.7,
        "A5": 8.3,
        "POWERPOINT": 6.667,
    }
    fig_width = widths[size.upper()]
    fig_height = fig_width * golden_mean  # height in inches\n",
    fig_size = [fig_width, fig_height]

    # plt.rcParams["image.cmap"]  = cm.batlow
    plt.rc("font", size=MEDIUM_SIZE)  # controls default text sizes\n",
    plt.rc("axes", titlesize=MEDIUM_SIZE)  # fontsize of the axes title\n",
    plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels\n",
    plt.rc("xtick", labelsize=SMALL_SIZE)  # fontsize of the tick labels\n",
    plt.rc("ytick", labelsize=SMALL_SIZE)  # fontsize of the tick labels\n",
    plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsize\n",
    plt.rc("figure", titlesize=BIGGER_SIZE)  # fontsize of the figure title\n",
    plt.rcParams.update(
        {
            "text.usetex": True,
            "font.family": "serif",
            "font.sans-serif": "Palatino",
        }
    )
    plt.rcParams["figure.figsize"] = fig_size
    plt.rcParams["figure.dpi"] = 200


if __name__ == "__main__":
    x = np.linspace(0, 2 * np.pi, 50)

    ys = {"Sin(x)": np.sin(x), "Cos(x)": np.cos(x)}
    fig, axes = plt.subplots(1, 2)

    labeler = panel_labeller()

    for ax, (key, y) in zip(axes.flatten(), ys.items()):
        ax.plot(x, y)
        ax.set_title(key)
        ax.set_xlabel("x")
        ax.set_ylabel(key)
        add_subfig_label(ax, labeler.next(), align="right")
    plt.tight_layout()
    plt.show()
