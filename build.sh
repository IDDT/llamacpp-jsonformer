#!/usr/bin/env bash


PLATFORM="$(uname -m)$(uname -s)"
PLATFORM="$(echo $PLATFORM | tr '[:upper:]' '[:lower:]')"


[ "$PLATFORM" = "arm64darwin" ]\
  && echo "Building with METAL support..." \
  && export LLAMA_METAL=1


COMMIT="3e5ca7931c68152e4ec18d126e9c832dd84914c8"
URL="https://github.com/ggerganov/llama.cpp/archive/$COMMIT.zip"
FILES=( "main" "ggml-metal.metal" )
wget -O llamacpp.zip $URL \
  && unzip llamacpp.zip && mv llama.cpp-$COMMIT llamacpp \
  && cd llamacpp && make -B LLAMA_DISABLE_LOGS=1 && cd .. \
  && for f in "${FILES[@]}"; do \
    mv "llamacpp/$f" "temp/$f"; done \
  && rm -rf llamacpp.zip llamacpp \
  && echo "Build succeeded." && exit 0 \
  || echo "Build failed." >&2 && exit 1
