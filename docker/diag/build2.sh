#!/usr/bin/env bash

docker build --build-arg DOCKER_RUNTIME=runc -t nnunetv2_local2 .
