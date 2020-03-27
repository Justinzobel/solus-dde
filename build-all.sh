#!/bin/bash
pushd () {
    command pushd "$@" > /dev/null
}

popd () {
    command popd "$@" > /dev/null
}

rootdir="$(pwd)/"

for i in $(cat ${rootdir}order)
  do
    pushd ${rootdir}${i}
    ypkg -f package.yml
    if [[ $(ls -1 *.eopkg | wc -l) -gt 0 ]]
      then
        echo ${i} >> ${rootdir}success
        eopkg it *.eopkg
        popd
      else
        echo ${i} >> ${rootdir}failures
    fi
done
