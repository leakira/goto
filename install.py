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

print 'Reading original file content'
sleep(2)
CURRENT_DIRECTORY = os.getcwd()
with io.open('goto.sh', 'r', encoding='utf-8') as f:
    data = f.read()

print 'Creating goto file in /usr/local/bin directory for direct call'
sleep(2)
data = data.replace('{{PATH}}', CURRENT_DIRECTORY)
path = '/usr/local/bin/goto'
outF = open(path, 'w')
outF.writelines(data)
outF.close()

os.system('chmod +x '+path)

print 'Install finished'