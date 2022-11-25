FROM nvcr.io/nvidia/tensorflow:22.10-tf2-py3

RUN python3 -m pip install autopep8 bandit black pylint
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/cuda-11.8/compat/lib.real

# Create a non-root user
ARG USERNAME=karaoker
ARG USER_UID=1000
ARG USER_GID=$USER_UID


# And let that user access the gpu and be sudo
RUN apt update && apt install sudo --yes --no-install-recommends && apt clean \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -G video \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
