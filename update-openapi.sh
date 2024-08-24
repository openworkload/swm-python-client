#!/usr/bin/env bash

set -x

function print_help() {
    echo "Usage:"
    echo "  1) Update from remote OpenAPI template file"
    echo "  $0"
    echo "  2) Update from local OpenAPI template file"
    echo "  $0 -l"
    exit 0
}

while getopts hl flag
do
    case "${flag}" in
        h) print_help;;
        l) ARG_LOCAL=1;;
    esac
done

. .venv/bin/activate

# Reliably get the script directory
pushd . > /dev/null
SCRIPT_DIR="${BASH_SOURCE[0]}"
if ([ -h "${SCRIPT_DIR}" ]); then
  while([ -h "${SCRIPT_DIR}" ]); do cd `dirname "$SCRIPT_DIR"`;
  SCRIPT_DIR=`readlink "${SCRIPT_DIR}"`; done
fi
cd `dirname ${SCRIPT_DIR}` > /dev/null
SCRIPT_DIR=`pwd`;
popd > /dev/null

# See https://github.com/openapi-generators/openapi-python-client
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
CONFIG=${SCRIPT_DIR}/openapi-python-client.yaml

if [ $ARG_LOCAL ]; then
  URL_ARG="--path $SCRIPT_DIR/../swm-core/priv/openapi.yaml"
else
  URL_ARG="--url https://raw.githubusercontent.com/openworkload/swm-core/${GIT_BRANCH}/priv/openapi.yaml"
fi

python3 $HOME/.local/bin/openapi-python-client update ${URL_ARG} --config $CONFIG --fail-on-warning
