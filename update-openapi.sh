#!/usr/bin/env bash

# Reliably get the script directory
pushd . > /dev/null
SCRIPT_DIR="${BASH_SOURCE[0]}"
if ([ -h "${SCRIPT_DIR}" ]); then
  while([ -h "${SCRIPT_DIR}" ]); do cd `dirname "$SCRIPT_DIR"`;
  SCRIPT_DIR=`readlink "${SCRIPT_DIR}"`; done
fi
cd `dirname ${SCRIPT_DIR}` > /dev/null
SCRIPT_DIR=`pwd`;
popd  > /dev/null

# See https://github.com/openapi-generators/openapi-python-client
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
URL=https://github.com/skyworkflows/swm-core/blob/master/priv/openapi.yaml
openapi-python-client --url $URL
#/home/taras/.local/bin/openapi-python-client generate --path ~/projects/swm-core/priv/openapi.yaml

#docker run --rm \
           #--volume ${SCRIPT_DIR}:/host-swm-core \
           #openapitools/openapi-generator-cli generate \
               #--generator-name python \
               #--input-spec /host-swm-core/priv/openapi.yaml \
               #--outpuy /host-swm-core/python/swmclient/generated/
