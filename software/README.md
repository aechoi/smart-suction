# capcup — smart suction cup software

Recording and analyzing capacitance data from the smart suction cup end
effector. See the [repository README](../README.md) for the full project
(hardware, firmware, software).

## Layout

```
software/
├── src/capcup/          installable package
│   ├── udp_receiver.py   live capture + plotting from the end effector
│   ├── simulator/        capacitance-probe forward simulation
│   └── jubilee/          ground-truth collection on the Jubilee platform
├── notebooks/           analysis notebooks (outputs stripped on commit)
│   └── experiments/      one notebook per historical experiment
├── models/             trained weights (gitignored; regenerate from notebooks)
├── figs/               generated figures (gitignored)
└── tests/
```

## Setup

Run from this `software/` directory.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS
python -m pip install --upgrade pip
pip install -e ".[dev,notebooks]"
```

`pip install -e .` alone installs just the runtime package. The Jubilee
scripts additionally need `jubilee_controller` (see `pyproject.toml`).

## Recording data

See [the repo README](../README.md#how-to-record-data) for the wiring. Then:

```bash
python -m capcup.udp_receiver -f my_capture.csv
```

Two windows open: a rolling time-domain plot and a radial plot. Captures
are written under `data/` (gitignored).

## Before pushing

```bash
pytest
ruff check .
```
