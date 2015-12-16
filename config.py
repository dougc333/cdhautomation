#!/usr/bin/env python

import sys
import argparse
from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.clusters import delete_cluster
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.parcels import get_parcel


from time import sleep
import re


def check(api):
  print "check config hdfs for FloodVolume"
  cm = ClouderaManager(api)
  cluster = cluster = api.get_cluster("HDDTest")
  hdfs_service = cluster.get_service("HDFS")
  hdfs_config = hdfs_service.get_config(view="Full")
  print hdfs_config


def cm_args_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--cm_host",default='r2341-d5-us01',help="url for host")
  parser.add_argument("--cm_user",default='admin', help='default user name')
  parser.add_argument("--cm_password",default='admin',help='default password for default user name')
  return parser


def main():
  parser = cm_args_parser()
  args = parser.parse_args()
  print "connecting to host:" + args.cm_host + "..."
  api = ApiResource(args.cm_host, username=args.cm_user, password=args.cm_password)
  print "done..."
  check(api)



if __name__ == '__main__':
  main()
  
