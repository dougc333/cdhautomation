#!/bin/bash -p

rm -rf /testdir/dfs
rm -rf /testdir2/dfs
rm -rf /tmp/hadoop-hdfs
ssh root@r2341-d5-us02 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us02 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us02 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us02 "rm -rf /dfs/dn"
ssh root@r2341-d5-us03 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us03 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us03 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us03 "rm -rf /dfs/dn"
ssh root@r2341-d5-us04 "rm -rf /testdir/dfs"
ssh root@r2341-d5-us04 "rm -rf /testdir2/dfs"
ssh root@r2341-d5-us04 "rm -rf /tmp/hadoop-hdfs"
ssh root@r2341-d5-us04 "rm -rf /dfs/dn"

