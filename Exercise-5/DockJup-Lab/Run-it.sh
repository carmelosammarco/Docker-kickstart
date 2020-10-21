#!/bin/bash

docker run -d -v "/${PWD}/Notebook:/SRC/Notebook" --name "dockjup-lab" -p 8888:8888 --restart always --shm-size 2g sicilian4ever/dockjup-lab