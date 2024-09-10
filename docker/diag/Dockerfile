FROM doduo1.umcn.nl/nnunet_for_pathology/sol2:latest

RUN echo "DefaultRuntime=${DOCKER_RUNTIME}"

RUN rm -rf \
/var/lib/docker/overlay2/*/merged/usr/lib/x86_64-linux-gnu/libnvidia-ml.so.1

ENTRYPOINT bash
