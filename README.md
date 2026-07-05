# 20260705_GitHub_Codespace_devcontainer_demo

## Demo 1 of 3 — Minimal mamba devcontainer (`demo/01-mamba-basic`)

The simplest possible useful devcontainer: a plain Ubuntu base image plus the
[`miniforge` devcontainer feature](https://github.com/rocker-org/devcontainer-features) (which
installs conda + [mamba](https://mamba.readthedocs.io/)), plus one small `environment.yml`. No
Dockerfile, nothing to build from scratch — the feature installs the package manager for us, we
just tell it what to install.

This is the first of three progressively more complex examples used in the companion talk, see
[`presentation_plan.md`](presentation_plan.md) on `main` for the full session outline.

### What's in here

- `.devcontainer/devcontainer.json` — uses `mcr.microsoft.com/devcontainers/base:ubuntu-22.04` as
  the base image, adds the `miniforge` feature to install conda/mamba, and runs `mamba install`
  once on container creation.
- `.devcontainer/environment.yml` — Python 3.11 + `samtools` (a real, small, fast-to-install
  bioinformatics CLI tool), pulled from `conda-forge` and `bioconda`.

### How to launch

**Option A — GitHub Codespaces**

1. On GitHub, make sure you're viewing the `demo/01-mamba-basic` branch.
2. Code → Codespaces → "Create codespace on branch".
3. Wait for the container to build (first time only, ~1-2 min).

**Option B — Locally with VS Code**

1. `git checkout demo/01-mamba-basic`
2. Open the folder in VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed.
3. Command palette → "Dev Containers: Reopen in Container".

Either way, `postCreateCommand` runs automatically and installs the environment for you — there is
nothing manual to run first.

### Verify it works

Once the container is up, open a terminal inside it and run:

```bash
mamba --version
mamba list -n base
samtools --version
```

You should see `samtools` report its version immediately, with no local install step on your part.

### Why this is useful

- Zero local setup: no need to have conda/mamba, or the right OS packages, installed on your own
  machine.
- The whole environment definition is two small text files, checked into git — anyone can
  reproduce exactly this setup by opening this branch.
- Good starting point when you only need one package manager and a couple of CLI tools — see
  `demo/02-mamba-python-r` for when you also need Python + R libraries side by side, and
  `demo/03-docker-dockerfile` for when you need OS-level control via a custom `Dockerfile`.
