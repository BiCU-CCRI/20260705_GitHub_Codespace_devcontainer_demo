# 20260705_GitHub_Codespace_devcontainer_demo

## Demo 3 of 3 — Dockerfile-based devcontainer (`demo/03-docker-dockerfile`)

The most advanced of the three examples: instead of pointing `devcontainer.json` at a ready-made
image (as in demos 1 and 2), we build our **own** image from a `.devcontainer/Dockerfile`. This is
the step you take once you need OS-level control that a prebuilt image can't give you — extra
system libraries, a non-default user flow, registered Jupyter kernels, additional forwarded ports.

See [`presentation_plan.md`](presentation_plan.md) for the full talk outline this demo belongs to.

### What's in here

- `.devcontainer/Dockerfile` — starts from the same `ubuntu-22.04` base image as demos 1 and 2,
  and adds:
  - system libraries needed by some R packages (`libcurl`, `libxml2`, `libssl`, build tools),
    installed as root, then drops back to the non-root `vscode` user;
  - Miniforge installed directly from the official installer script (the same `mamba` you get from
    the `miniforge` feature in demos 1/2 — it's installed manually here because devcontainer
    features only apply *after* a custom Dockerfile build finishes, so the feature itself isn't
    available yet inside these `RUN` steps);
  - the same style of `environment.yml`-driven install as before, plus `jupyterlab`;
  - a registered Python **and** R Jupyter kernel, so both languages show up side by side in one
    JupyterLab instance.
- `.devcontainer/environment.yml` — Python + R + libraries (as in demo 2), plus `jupyterlab`,
  `ipykernel`, `r-irkernel`, and `bcftools` as an extra bioinformatics CLI tool.
- `.devcontainer/devcontainer.json` — points `build.dockerfile` at the Dockerfile above and
  forwards port `8888` for JupyterLab.
- `scripts/demo.py` / `scripts/demo.R` — same small demo scripts as demo 2, usable directly or
  from a notebook via the registered kernels.

### How to launch

**Option A — GitHub Codespaces**

1. On GitHub, make sure you're viewing the `demo/03-docker-dockerfile` branch.
2. Code → Codespaces → "Create codespace on branch".
3. Wait for the image to build. This is the slowest of the three demos to build the first time,
   since it compiles a custom image rather than pulling one ready-made — pre-warm it before a live
   presentation, or set up a Codespaces **prebuild** for a large audience.

**Option B — Locally with VS Code**

1. `git checkout demo/03-docker-dockerfile`
2. Open the folder in VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.
3. Command palette → "Dev Containers: Reopen in Container" (this will run `docker build` locally
   using the Dockerfile above).

### Verify it works

```bash
python scripts/demo.py
Rscript scripts/demo.R
bcftools --version
```

Then start JupyterLab and use VS Code's forwarded-ports notification (or open
`http://localhost:8888` yourself) to reach it in your browser:

```bash
jupyter lab --ip=0.0.0.0 --no-browser
```

Inside JupyterLab, check the kernel picker — both "Demo 03 (Python)" and "Demo 03 (R)" should be
available in the same environment.

### Why this is useful

- Full control: OS packages, non-root user setup, additional services, and forwarded ports are all
  things a plain `image:` reference can't express — a `Dockerfile` can.
- Still fully reproducible and still "one command to launch it" for anyone opening this branch,
  even though there's a real image build happening under the hood.
- The natural end of the ladder from this series: `demo/01-mamba-basic` (ready-made image) →
  `demo/02-mamba-python-r` (richer environment, same image) → this branch (custom image via
  Dockerfile). Pick the lowest rung that solves your actual problem.
