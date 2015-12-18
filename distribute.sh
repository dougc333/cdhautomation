#!/bin/bash -p

# the datanodes have to be in this file

datanodes=('r2341-d5-us02' 
           'r2341-d5-us03' 
           'r2341-d5-us04');


for nodes in ${datanodes[@]};do
    printf "copying directory to $nodes \n"
    scp -r /root/cdhautomation root@$nodes:/root 
done

