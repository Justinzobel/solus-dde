#!/bin/bash
pushd () {
    command pushd "$@" > /dev/null
}

popd () {
    command popd "$@" > /dev/null
}

rootdir="$(pwd)/"
mkdir ${rootdir}/bin

buildfile=order-group5

for i in $(cat ${rootdir}${buildfile})
  do
    pushd ${rootdir}${i}
    # solbuild build -p main-x86_64 package.yml
    ypkg -f package.yml
    if [[ $(ls -1 *.eopkg | wc -l) -gt 0 ]]
      then
        echo ${i} >> ${rootdir}success
        mv *.eopkg ${rootdir}/bin/
        popd
        #pushd /var/lib/solbuild/local
        #eopkg index --skip-signing .
        #spopd
      else
        echo ${i} >> ${rootdir}failures
    fi
    rm -rf ~/YPKG/sources/*
    #read -p "Continue? " answer
done
