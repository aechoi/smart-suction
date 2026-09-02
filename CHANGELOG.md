# Changelog

## Repo cleanup — 2026-09-02

Reorganized from an ad-hoc layout into a hardware/firmware/software monorepo.

### Structure
- `software/` now holds the Python side (package, notebooks, tests); was the
  repo root.
- `firmware/` added — the ESP32 end-effector Arduino sketch.
- `hardware/` unchanged; `assets/` → `docs/`.
- Package `capcup`: `jubliee_scripting/` renamed to `jubilee/`, notebooks and
  `figs/` moved out of the importable package.

### Removed
- 95 KiCad auto-backup zips, stale gerber/vendor zips, `fp-info-cache`,
  `*.kicad_prl`, autosaves — all recoverable from history.
- Trained weights (`*.pt`) and generated `figs/` are no longer tracked.
- Serial capture and eval-board data-processing code — see tag
  `archive/serial-and-eval-pipeline`.

### Tooling
- `pyproject.toml`: correct package path, real dependencies, `[dev]` /
  `[notebooks]` extras, ruff + pytest config, `capcup-record` entry point.
- Added `.pre-commit-config.yaml` (ruff, nbstripout, hygiene) and a
  GitHub Actions CI workflow.
- `.gitattributes` for line-ending normalization.
- Notebook outputs stripped from the active notebooks; experiment records
  under `software/notebooks/experiments/` keep theirs.
