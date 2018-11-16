#!/usr/bin/env python

################
### goto.py Install script
###   Will install script in /usr/local/bin directory for direct call
################

import io, os
from os.path import expanduser
from time import sleep

print 'Starting install'
sleep(1)

print 'Copying scripts to /usr/local/bin directory for direct call'
os.system('cp -v _goto.py /usr/local/bin/_goto.py')
os.system('cp -v goto.sh /usr/local/bin/goto')
sleep(2)

print 'Install finished'