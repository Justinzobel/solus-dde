#!/bin/bash

iteration=10

echo "Testing with ${iteration} iterations"
echo

echo "No caching"
time {
    for n in $(seq 1 ${iteration}); do
        if [ -e '.packagecache' ]; then
            rm .packagecache
        fi
        solus-package-util build avfs &> /dev/null
    done
}

echo
echo "With caching"

time {
    for n in $(seq 1 ${iteration}); do
        solus-package-util build avfs &> /dev/null
    done
}

exit
