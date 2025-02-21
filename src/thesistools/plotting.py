# thesistools/plotting.py
"""_summary_
A collection of plotting tools for the Latex Thesis template
Author: Blair Haydon 2025
"""

from string import ascii_lowercase
import numpy as np


class panel_labeller:
    """
    Class for generating sequential labels for plot panels.
    """

    def __init__(self, sequence=ascii_lowercase):
        self.sequence = sequence
        self._label_index = 0

    def next(self):
        """
        Get the next label in the sequence.
        Returns:
            str: The next label.
        """
        label = self.sequence[self._label_index]
        self._label_index += 1
        return label


def add_subfig_label(ax, label:str,facecolor="0.7",edgecolor="none", alpha=0.5,*args, **kwargs):
    """
    Add a label to a subfigure.

    Parameters:
        ax (mpl.axes.Axes): The subplot axis to label.
        label (str): The label text.
        description (str, optional): Additional description text.
    """
    ax.annotate(
        f"{label})",
        xy=(0, 1),
        xycoords="axes fraction",
        xytext=(+0.5, -0.5),
        textcoords="offset fontsize",
        fontsize="medium",
        verticalalignment="top",
        fontfamily="serif",
        bbox=dict(facecolor=facecolor, edgecolor=edgecolor, pad=3.0, alpha=alpha,*args, **kwargs),
    )


def set_size(aspect:[float | str]="wide"):
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


def dose(termination: str = "Oxygen") -> np.ndarray:

    DOSE_PER_SECOND = 21.741378420061995  # mJ/s/cm2
    if termination == "Oxygen":
        exposures = np.concatenate(  # Explosure duration in seconds from beamtime excel datasheet
            (
                np.zeros(1),
                np.ones(2) * 221,
                np.ones(2) * 442,
                np.ones(2) * 884,
                np.ones(1) * 1768,
            )
        )

    dose = np.zeros(len(exposures))  # Array for each exposure
    for i, j in enumerate(
        exposures
    ):  # Update array positions with cumulative dose at said point
        dose[i] = (j * DOSE_PER_SECOND) + np.sum(dose)
    return np.array(dose)
