#!/usr/bin/env bash

PLATFORM="$(uname -m)$(uname -s)"
PLATFORM="$(echo $PLATFORM | tr '[:upper:]' '[:lower:]')"


[ "$PLATFORM" = "arm64darwin" ]\
  && echo "Building with METAL support..." \
  && export LLAMA_METAL=1

COMMIT="41c674161fb2459bdf7806d1eebead15bc5d046e"
cd temp && wget -O llamacpp.zip https://github.com/ggerganov/llama.cpp/archive/$COMMIT.zip \
  && unzip llamacpp.zip && mv llama.cpp-$COMMIT llamacpp \
  && cd llamacpp && make && mv main ../binary && cd .. \
  && echo "Build successfull."

LIB_METAL=llamacpp/ggml-metal.metal
[ -f $LIB_METAL ] && cp $LIB_METAL .

rm -rf llamacpp
