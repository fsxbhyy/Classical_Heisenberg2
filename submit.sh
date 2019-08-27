#!/bin/bash

#BSUB -n 1
#BSUB -W 32:00
#BSUB -q long
#BSUB -J "Jobq1[1-639]"
#BSUB -i "input.%I"
#BSUB -o logs/out.%J.%I
#BSUB -e logs/err.%J.%I

./main

