#!/usr/bin/env python

#adds HDFS, Impala,Hive, YARN services
#install services; print out role config groups, fix customization for each RCG
#redo w/install services

import sys
import argparse
from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException
from testdssdscr import add_hosts
from testdssdscr import add_parcels




#assume Cloudera Management Service already installed


def checkServices(api):
  #cluster = api.create_cluster("HDDTest", version="CDH5")
  cluster = api.get_cluster("HDDTest")
  service_types = cluster.get_service_types()
  print "service_types:", service_types
  all_services = cluster.get_all_services(view="Full")
  print "all services:", all_services 
  host_templates = cluster.get_all_host_templates()
  print "host_templates:", host_templates 


def cm_args_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--cm_host",default="r2341-d5-us01", help="")
  parser.add_argument("--cm_user",default="admin",help="")
  parser.add_argument("--cm_password",default="admin",help="")
  return parser

def main():
   print "test services in cluster"
   parser = cm_args_parser()
   args = parser.parse_args()
   print "connecting to host:" +args.cm_host + "..."
   api = ApiResource(args.cm_host, username=args.cm_user, password = args.cm_password)
   print "done...."
   checkServices(api)
   add_hosts(api)
   add_parcels(api)
 
if __name__=='__main__':
  main()
  


