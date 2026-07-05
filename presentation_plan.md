# GitHub Codespaces & `.devcontainer` — 25-Minute Presentation Plan

A short talk + live demo aimed at a bioinformatics-adjacent audience (wet-lab-turned-dry-lab
scientists, rotation students, core facility staff). Goal: show that a `.devcontainer` is a small,
versionable file that eliminates "works on my machine" for analysis environments, then prove it
with three progressively more complex, real, working examples in this repo.

## Timing overview (25 min total)

| # | Segment                                              | Time  |
|---|-------------------------------------------------------|-------|
| 1 | Intro & hook                                          | 3 min |
| 2 | Why this matters (bioinformatics angle)               | 5 min |
| 3 | Anatomy of a `.devcontainer`                          | 2 min |
| 4 | Demo 1 — minimal mamba devcontainer                   | 4 min |
| 5 | Demo 2 — mamba + Python + R                           | 5 min |
| 6 | Demo 3 — Dockerfile-based, full control               | 5 min |
| 7 | Wrap-up, recap, Q&A buffer                            | 1 min |

## 1. Intro & hook (3 min)

- Open with the universal pain: *"it installs fine on my laptop, breaks on yours, and breaks
  again in six months on my own laptop after an OS update."*
- One-sentence definitions:
  - **Codespace** = a full dev environment running in the cloud (or locally), started from your repo.
  - **`.devcontainer`** = the config file(s) in your repo that describe exactly what that environment
    contains (OS packages, language runtimes, VS Code extensions, startup commands).
- Preview the structure of the talk: 3 branches in this repo, each one is a real, runnable example,
  each one a notch more advanced than the last.

## 2. Why this matters — bioinformatics angle (5 min)

- **Reproducibility of pipelines.** The classic conda/R/Bioconductor version-hell problem — a
  `devcontainer.json` + `environment.yml` pins the *entire* toolchain, not just a package list.
- **Onboarding.** A rotation student or new hire doesn't spend day one installing R, conda, and
  system libraries — they click "Create codespace" and get a working RStudio/Jupyter-capable
  environment in minutes.
- **Reviewer / collaborator reproducibility.** A paper or shared analysis repo with a working
  devcontainer means a reviewer or collaborator can literally open the repo and rerun the analysis
  without touching their own machine's Python/R install.
- **Heterogeneous hardware.** Lab laptops are a mix of Intel Mac, Apple Silicon, Windows, locked-down
  institute machines. The container abstracts that away — same environment everywhere.
- **Isolation.** Multiple projects needing conflicting R/Bioconductor or Python versions no longer
  fight each other on one machine.
- Brief caveat: Codespaces has a free tier and then compute/storage billing — worth a one-line
  mention so nobody is surprised, plus that everything shown today also works as a **local**
  "Reopen in Container" with just Docker + VS Code, no GitHub billing involved.

## 3. Anatomy of a `.devcontainer` (2 min)

Show (on screen, not yet running) the shape of a `devcontainer.json`:

- `image` **or** `build.dockerfile` — where the container comes from.
- `features` — optional pre-packaged add-ons (not used in these demos, but worth a mention).
- `postCreateCommand` — shell command(s) run once after the container is built (e.g. create the
  package environment).
- `customizations.vscode.extensions` — VS Code/Codespaces extensions installed automatically.
- `forwardPorts` — expose a port (e.g. Jupyter) from inside the container to your browser.
- Where it lives: `.devcontainer/devcontainer.json` in the repo root.
- Two ways to launch the *same* config: GitHub → "Create codespace on branch", or locally via the
  VS Code "Dev Containers: Reopen in Container" command.

## 4. Demo 1 — minimal mamba devcontainer (4 min)

Branch: `demo/01-mamba-basic`

- Show `.devcontainer/devcontainer.json` (base image is a ready-made micromamba image — nothing to
  install, mamba is already there) and `.devcontainer/environment.yml` (just Python + `samtools`).
- Launch it (Codespaces or local reopen-in-container).
- Once inside, run:
  - `micromamba --version`
  - `micromamba list`
  - `samtools --version`
- **Message:** one small file gets you a real bioinformatics CLI tool, installed and ready, with
  zero local setup.

## 5. Demo 2 — mamba + Python + R (5 min)

Branch: `demo/02-mamba-python-r`

- Show the richer `environment.yml`: Python (pandas, biopython) + R (data.table, ggplot2, dplyr).
- Show the added VS Code extensions for Python and R in `devcontainer.json`.
- Launch it, then run the two provided demo scripts:
  - `python .devcontainer/../scripts/demo.py` (or open in VS Code and run) — reverse-complements a
    toy sequence, prints a small expression table.
  - `Rscript scripts/demo.R` — builds the same toy table in `data.table`, saves a `ggplot2` bar
    chart.
- **Message:** two languages that bioinformatics constantly needs together (R for stats/plots,
  Python for wrangling/pipelines) coexist in one reproducible, declarative environment.

## 6. Demo 3 — Dockerfile-based, full control (5 min)

Branch: `demo/03-docker-dockerfile`

- Explain the escalation: sometimes a prebuilt image isn't enough — you need specific system
  libraries (e.g. `libcurl`, `libxml2` for R packages), a Jupyter kernel registered, extra ports
  forwarded. That's when you graduate from `image:` to `build.dockerfile:`.
- Show `.devcontainer/Dockerfile`: installs system deps as root, drops back to the non-root mamba
  user, installs the same style of env plus JupyterLab, registers Python + R kernels.
- Show `devcontainer.json`'s `forwardPorts: [8888]`.
- Launch it (mention: first build is a little slower — this is where GitHub Codespaces
  "prebuilds" would help in a real project, so pre-warm this one before presenting live).
- Once inside: `jupyter lab --ip=0.0.0.0 --no-browser`, open the forwarded port, show both an R and
  a Python kernel available in the same JupyterLab instance.
- **Message:** the same "one command to reproduce" promise still holds, even once you need OS-level
  control — you've just moved the recipe into a Dockerfile instead of picking an off-the-shelf image.

## 7. Wrap-up & Q&A (1 min buffer)

- Recap the ladder: **ready-made image → richer environment on the same image → custom
  Dockerfile for full control.** Pick the lowest rung that solves your problem.
- Call to action: try "Reopen in Container" on one of your own analysis repos this week, or clone
  one of these three branches as a starting point.
- Open floor for questions.

## Presenter prep checklist (do this before the session, not live)

- [ ] Pre-build/open each of the 3 branches once beforehand so the Codespace image is cached
      (or use GitHub Codespaces **prebuilds** if presenting to a large group).
- [ ] Have a screen recording or screenshots of a successful build as a fallback in case of
      network flakiness during the live session.
- [ ] Confirm Codespaces access/quota for anyone in the audience who wants to follow along, and
      have the local "Dev Containers: Reopen in Container" path ready as a backup for anyone
      without Codespaces access.
- [ ] Sanity-check all three branches build cleanly right before presenting (conda-forge/bioconda
      channels and package versions can drift).

## Branch reference

| Branch                        | What it adds                                             |
|--------------------------------|-----------------------------------------------------------|
| `demo/01-mamba-basic`          | micromamba base image + minimal `environment.yml`         |
| `demo/02-mamba-python-r`       | + Python and R side by side, several R/Python libraries   |
| `demo/03-docker-dockerfile`    | + custom `Dockerfile`, system libs, Jupyter, forwarded port|
