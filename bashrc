#!/bin/bash 

if [ -n "$ZSH_VERSION" ]; then
    export IVIZ_PATH="$( cd "$( dirname "${(%):-%N}" )" && pwd )"
else
    export IVIZ_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
fi

export PYTHONPATH="$IVIZ_PATH/python:$PYTHONPATH"
export PATH="$IVIZ_PATH/bin:$PATH"

