#!/usr/bin/env bash

PLATFORM="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH="$(uname -m)"

[ "$ARCH$PLATFORM" = "arm64darwin" ]\
  && echo "Building with METAL support..." \
  && export LLAMA_METAL=1

COMMIT="b2e071dd86f4e934e5eb0755d57067567a88d5ce"
cd temp && wget -O llamacpp.zip https://github.com/ejones/llama.cpp/archive/$COMMIT.zip \
  && unzip llamacpp.zip && mv llama.cpp-$COMMIT llamacpp \
  && cd llamacpp && make && mv main ../binary \
  && cd .. && rm -rf llamacpp \
  && echo "Build finished successfully."
