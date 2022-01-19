#!/bin/bash
set -x # echo on

CPY="python /home/ameyer/src/python/cpy/cpy.py"
PST="python /home/ameyer/src/python/cpy/pst.py"

$CPY cpy.py cpy.py -c
rm dest/*
$PST dest -v

$CPY dest -c
$PST dest2
$PST dest2 -f
$PST dest2
