# Demo 3: full control via a custom Dockerfile, instead of just picking a ready-made image.
# Starting point is still the micromamba image (same as demos 1 and 2), but here we also
# need OS-level system libraries and a registered Jupyter kernel, so we build our own layer.
FROM mambaorg/micromamba:1.5.8-bookworm

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

USER $MAMBA_USER
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml -c conda-forge -c bioconda \
    && micromamba clean --all --yes

RUN micromamba run -n base python -m ipykernel install --user \
    --name demo03-python --display-name "Demo 03 (Python)"
RUN micromamba run -n base R -e "IRkernel::installspec(name = 'demo03-r', displayname = 'Demo 03 (R)')"
