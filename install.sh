#!/usr/bin/env bash

################
### Script for remote install
################

curl -o goto-master.zip https://codeload.github.com/leakira/goto/zip/master
unzip goto-master.zip
cd goto-master && sudo ./install.py
cd ..
rm goto-master.zip
rm -rf goto-master
