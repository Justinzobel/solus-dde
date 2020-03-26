#!/bin/bash
rootdir="/home/justin/Builds/solus-dde/"
watch 'echo "Successful:" && tail -n 10 ${rootdir}success && echo && echo "Total eopkgs: $(ls -l /var/lib/solbuild/local/*.eopkg | wc -l)" && echo && if [[ -e ${rootdir}failures ]];then echo Failures && tail -n 10 ${rootdir}failures;fi'
