# Demo 3: full control via a custom Dockerfile, instead of just picking a ready-made image or
# devcontainer feature. Installs mamba (via the official Miniforge installer) directly in the
# Dockerfile - this is the step you take once you need OS-level control that a plain image or
# feature can't give you.
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

USER root
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -L -o /tmp/miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh \
    && bash /tmp/miniforge.sh -b -p /opt/conda \
    && rm /tmp/miniforge.sh \
    && chown -R vscode:vscode /opt/conda
ENV PATH=/opt/conda/bin:$PATH

USER vscode
COPY --chown=vscode:vscode environment.yml /tmp/environment.yml
RUN mamba install -y -n base -f /tmp/environment.yml -c conda-forge -c bioconda \
    && mamba clean --all --yes
