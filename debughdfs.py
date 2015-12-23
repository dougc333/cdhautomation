#!/usr/bin/env python

#debug hdfs setup, download rcgs
#install hdfs (nondssd and print out)
# install datanode and print

from cm_api.api_client import ApiResource
from cm_api.endpoints.clusters import ApiCluster
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.parcels import ApiParcel
from cm_api.endpoints.parcels import get_parcel
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiService, ApiServiceSetupInfo
from cm_api.endpoints.services import create_service
from cm_api.endpoints.types import ApiCommand, ApiRoleConfigGroupRef
from cm_api.endpoints.role_config_groups import get_role_config_group
from cm_api.endpoints.role_config_groups import ApiRoleConfigGroup
from cm_api.endpoints.roles import ApiRole
from time import sleep

import re



def get_info(api):
  cluster = api.get_cluster("HDDTest")
  cm = api.get_cloudera_manager()
  all_services = cluster.get_all_services(view="Full")
  print "all_services:", all_services
  for service in all_services:
    print "service config:", service.get_config(view="Full")
    list_rcg = service.get_all_role_config_groups()
    print "role config groups:", list_rcg  
    for rcg in list_rcg:
      print "rcg:",rcg, " rcg config:", rcg.get_config(view="Full")    
      list_roles = rcg.get_all_roles()
      print "list_roles:", list_roles
      for r in list_roles:
        print "role:", r, " config:", r.get_config(view="Full")

def main():
  """ 
  """
  api=ApiResource('r2341-d5-us01',username='admin')
  get_info(api)

if __name__=="__main__":
  main()
