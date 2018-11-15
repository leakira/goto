#!/usr/bin/env bash

################
### Bash script for goto.py
###   Python script not works well with terminal "source" command,
###   so use this script to turns working path navigation
################

PATH={{PATH}}

# Catch python script response
output=$(${PATH}/goto.py "$@" 2>&1)

# Validate if has space to identify run path
if [[ ${output} = *[\ ]* ]]; then
  # If is simple response, simply echo
  echo "$output"
else
  # If is run path, run "cd" command. Need to call with "source" command
  cd ${output}
fi
