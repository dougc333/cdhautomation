#!/bin/bash -p

# we need this before NN format for starting dssd datanode hdfs 
# 

rm -rf /testdir/dfs
rm -rf /testdir2/dfs
rm -rf /tmp/hadoop-hdfs
rm -rf /var/run/hdfs-sockets
ssh root@r2341-d5-us02 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us02 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us02 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us02 "rm -rf /dfs/dn"
ssh root@r2341-d5-us02 "rm -rf /var/run/hdfs-sockets"
ssh root@r2341-d5-us03 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us03 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us03 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us03 "rm -rf /dfs/dn"
ssh root@r2341-d5-us03 "rm -rf /var/run/hdfs-sockets"
ssh root@r2341-d5-us04 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us04 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us04 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us04 "rm -rf /dfs/dn"
ssh root@r2341-d5-us04 "rm -rf /var/run/hdfs-sockets"

