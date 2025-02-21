# Thesistools

## Version 0.1.1

- Adds installation of custom matplotlib style sheet

## Installation
Building this package with [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager is recommended.


Clone reop with

`git clone https://github.com/blairium/thesistools.git
cd thesistools`

Run the command

`uv build`

Then

`pip install .\dist\thesistools-0.1.1-py3-none-any.whl`

## Usage

- This installs the matplotlib style thesis which can be used with
`plt.style.use('thesis')` This is a modified version of https://github.com/garrettj403/SciencePlots/
- Label subplots:
  
  `from thesistools.plotting import panel_labeller,add_subfig_label`


Inititate label before plotting.
`label = panel_labeller()`


Call `add_subfig_label` after each plot.
`add_subfig_label(ax, label.next())`

`add_subfig_label` takes all the keyword arguements that matplotlibs annotate takes. `facecolor=0.5,alpha=0.5` are the defaults. They grey box can be turned off with `facecolor='none'`


