#!/usr/bin/env bash

PLATFORM="$(uname -m)$(uname -s)"
PLATFORM="$(echo $PLATFORM | tr '[:upper:]' '[:lower:]')"


[ "$PLATFORM" = "arm64darwin" ]\
  && echo "Building with METAL support..." \
  && export LLAMA_METAL=1


COMMIT="11315b1d61352944791db9c81db1b7bd8bd39f2e"
cd temp && wget -O llamacpp.zip https://github.com/ejones/llama.cpp/archive/$COMMIT.zip \
  && unzip llamacpp.zip && mv llama.cpp-$COMMIT llamacpp \
  && cd llamacpp && make && mv main ../binary && cd .. \
  && echo "Build successfull."

LIB_METAL=llamacpp/ggml-metal.metal
[ -f $LIB_METAL ] && cp $LIB_METAL .

rm -rf llamacpp
