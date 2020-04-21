#!/bin/bash
rootdir="/home/justin/Builds/solus-dde/"

function success {
  if [[ -e ${rootdir}success ]] 
    then
      echo "Successful ($(wc -l success | cut -d " " -f 1)):" && tail -n 10 ${rootdir}success
    else
      echo "No successful builds yet."
  fi
  echo
}

function failures {
  if [[ -e ${rootdir}failures ]]
    then
      echo "Failures ($(wc -l failures | cut -d " " -f 1)):" && tail -n 10 ${rootdir}failures
    else
      echo "No failures so far, hoorah!"
  fi
}

success
failures