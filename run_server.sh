#!/bin/bash
usage="Usage: ./run_server.sh <port>"
if [[ $1 == "" ]]; then
    echo "${usage}"
else
    standalone.py -p $1 -d server
fi
