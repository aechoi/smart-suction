# Experiment records

One notebook per experiment run, kept as a frozen record — **rendered output
is committed on purpose** (these are excluded from the `nbstripout`
pre-commit hook).

## Adding a new experiment

For anything you want to refer back to later, make a folder:

```
experiments/2026-09-15_electrode-spacing/
├── README.md      what was tested, hardware/rig config, raw-data location
├── analysis.ipynb the notebook
└── report.html    executed notebook, exported  (the permanent record)
```

Export the rendered report with:

```bash
python -m nbconvert --to html --output report.html analysis.ipynb
```

Reusable analysis code (loading a capture, SNR, standard plots) belongs in
`capcup`, not copied between notebooks. Raw captures stay out of git — note
their location in the experiment README.

## Existing notebooks

The loose `*.ipynb` here predate this convention; they are kept as-is.
