#!/bin/bash
pushd () {
    command pushd "$@" > /dev/null
}

popd () {
    command popd "$@" > /dev/null
}

rootdir="/home/justin/Builds/solus-dde/"
mkdir -p ${rootdir}eopkgs

for i in $(cat ${rootdir}order)
  do
    pushd ${rootdir}${i}
    make local
    if [[ $(ls -1 *.eopkg | wc -l) -gt 0 ]]
      then
        echo ${i} >> ${rootdir}success
        mv *.eopkg /var/lib/solbuild/local/
        popd
      else
        echo ${i} >> ${rootdir}failures
    fi
done
