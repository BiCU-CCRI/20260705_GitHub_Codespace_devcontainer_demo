# 20260705_GitHub_Codespace_devcontainer_demo

## Demo 2 of 3 — mamba + Python + R devcontainer (`demo/02-mamba-python-r`)

A step up from `demo/01-mamba-basic`: the same micromamba base image, but the `environment.yml`
now installs **both** Python and R, plus a few libraries from each, so the two languages
bioinformatics most often needs together — Python for wrangling/pipelines, R for stats/plots —
coexist in one reproducible environment.

See [`presentation_plan.md`](presentation_plan.md) for the full talk outline this demo belongs to.

### What's in here

- `.devcontainer/devcontainer.json` — same `mambaorg/micromamba` base image as demo 1, plus VS
  Code extensions for both Python and R.
- `.devcontainer/environment.yml` — Python 3.11 (`pandas`, `biopython`) and R 4.3
  (`r-ggplot2`, `r-data.table`, `r-dplyr`).
- `scripts/demo.py` — tiny Python script: reverse-complements a toy DNA sequence with Biopython,
  prints a small expression table with pandas.
- `scripts/demo.R` — tiny R script: builds the same toy table with `data.table` and saves a
  `ggplot2` bar chart.

### How to launch

**Option A — GitHub Codespaces**

1. On GitHub, make sure you're viewing the `demo/02-mamba-python-r` branch.
2. Code → Codespaces → "Create codespace on branch".
3. Wait for the container to build (first time only, a few minutes — installing R + Python
   together takes a bit longer than demo 1).

**Option B — Locally with VS Code**

1. `git checkout demo/02-mamba-python-r`
2. Open the folder in VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.
3. Command palette → "Dev Containers: Reopen in Container".

`postCreateCommand` installs the full environment automatically — nothing manual to run first.

### Verify it works

```bash
python scripts/demo.py
Rscript scripts/demo.R
```

The Python script prints a reverse-complemented sequence and a small table. The R script prints
the same style of table and writes `expression_demo.png` — open it in VS Code to see the bar chart.

### Why this is useful

- One declarative file (`environment.yml`) instead of two separate, easy-to-drift install
  procedures for Python and R.
- New lab members or students get a working Python **and** R analysis environment on day one,
  without installing either from scratch.
- A natural middle ground: still no custom `Dockerfile` needed, just a richer package list on top
  of the same base image as demo 1. When you need OS-level control (system libraries, extra
  services, custom users), see `demo/03-docker-dockerfile`.
