# Demo 3: full control via a custom Dockerfile, instead of just picking a ready-made image or
# devcontainer feature. Same install method as demos 1 and 2 (Ubuntu base + Miniforge -> mamba),
# but baked into our own Dockerfile: devcontainer features are applied *after* a custom Dockerfile
# build, so they can't be relied on inside RUN steps here - we install Miniforge ourselves instead.
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev \
    curl \
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

RUN mamba run -n base python -m ipykernel install --user \
    --name demo03-python --display-name "Demo 03 (Python)"
RUN mamba run -n base R -e "IRkernel::installspec(name = 'demo03-r', displayname = 'Demo 03 (R)')"
