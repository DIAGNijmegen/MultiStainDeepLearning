# Use the NVIDIA CUDA image as the base image
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

# Set noninteractive mode for apt-get
ARG DEBIAN_FRONTEND=noninteractive

# Update package lists and install required packages
RUN apt-get update && apt-get install -y \
    libcrypto++-dev \
    libgomp1 \
    libopenblas0-openmp \
    libvips-dev \
    openslide-tools \
    python3 \
    python3-pip \
    git \
    wget \
    libgeos-dev \
    && apt-get clean

# Install required system packages
RUN apt-get install -y libprotobuf-dev protobuf-compiler

# Install PyTorch and torchvision with CUDA support
RUN pip3 install --no-cache-dir torch==1.11.0 torchvision==0.12.0 torchaudio --extra-index-url https://download.pytorch.org/whl/cu111

# Install additional Python packages
RUN pip3 install --no-cache-dir \
    numpy==1.19.3 \
    lifelines==0.25.7 \
    scikit-learn \
    matplotlib==3.3.4 \
    pandas==0.24.2 \
    tqdm==4.64.0 \
    tensorboard==2.1.0 \
    Pillow==7.1.2 \
    captum==0.4.0 \
    black \
    isort \
    jupyterlab-code-formatter \
    ipywidgets \
    ipympl \
    shapely==1.7.1

# Set the working directory
WORKDIR /usr/src/app

# Copy the local project folder to the Docker image
COPY --chown=root:root . /usr/src/app

# Download and install the ASAP package
RUN mkdir -p /usr/src/app/asap && \
    wget "https://github.com/computationalpathologygroup/ASAP/releases/download/ASAP-2.1-(Nightly)/ASAP-2.1-Ubuntu2204.deb" -O /usr/src/app/asap/ASAP-2.1-Ubuntu2204.deb && \
    apt-get install --assume-yes /usr/src/app/asap/ASAP-2.1-Ubuntu2204.deb && \
    ldconfig && \
    SITE_PACKAGES=$(python3 -c "import sysconfig; print(sysconfig.get_paths()['purelib'])") && \
    printf "/opt/ASAP/bin/\n" > "${SITE_PACKAGES}/asap.pth" && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose necessary ports (e.g., JupyterLab port)
EXPOSE 8888

# Set the working directory to /usr/project_sync, this is where we will mount the project root folder to so we keep the project synced
WORKDIR /usr/home/project_sync
ENV HOME="/usr/home"

# Set the entrypoint to a bash shell
ENTRYPOINT ["/bin/bash"]
