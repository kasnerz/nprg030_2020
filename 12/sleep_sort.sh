#!/usr/bin/env bash

arr=(5 1 10 2 4 3)

function sleep_sort {
    sleep "$1" && echo -n "$1 "
}

for number in "${arr[@]}"; do
   sleep_sort $number &
done