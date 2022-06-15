#!/bin/bash
# profiles the program  assuming you've added the @profile decorator
mprof run recursive/recursive_indexer.py
# plots the memory usage in respect to time
mprof plot
echo "Cleaning up!"
sleep 1
rm *.dat