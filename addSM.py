#!/usr/bin/env python


#add cloudera manager service
#the code examples dont work; have to debug by look ing at all the services which are added 





import sys
import argparse
import subprocess

from cm_api.api_client import ApiResource
from cm_api.endpoints.clusters import ApiCluster
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.parcels import ApiParcel
from cm_api.endpoints.parcels import get_parcel
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.services import ApiService, ApiServiceSetupInfo
from cm_api.endpoints.services import create_service

from cm_api.api_client import ApiResource
from cm_api.api_client import ApiException
from cm_api.endpoints.clusters import create_cluster
from cm_api.endpoints.clusters import delete_cluster
from cm_api.endpoints.cms import ClouderaManager
from cm_api.endpoints.parcels import get_parcel



from time import sleep
import re







def addSM(api):
  """
  """
  cm = ClouderaManager(api)
  cluster = api.get_cluster("HDDTest")
  service_setup = ApiServiceSetupInfo(name="MGMT", type="MGMT")
  cm.create_mgmt_service(service_setup)
  #cluster.auto_assign_roles()
  #cluster.auto_configure()  
  cm_service = cm.get_service()
  cm_service.start().wait()

  rm_role = None
    for r in cm.get_service().get_all_roles():
        if r.type == "REPORTSMANAGER":
            rm_role = r

    if rm_role == None:
      print "No REPORTSMANAGER role found!"
        exit(0)

  rm_role_group = rm_role.roleConfigGroupRef
    rm_rcg = get_role_config_group(api, rm_role.type, \
                rm_role_group.roleConfigGroupName, None)

    # update the appropriate fields in the config
    rm_rcg_config = { "headlamp_database_host" : reports_manager_host, \
                      "headlamp_database_name" : reports_manager_name, \
                      "headlamp_database_user" : reports_manager_username, \
                      "headlamp_database_password" : reports_manager_password, \
                              "headlamp_database_type" : reports_manager_database_type }

    rm_rcg.update_config(rm_rcg_config)


    # restart the management service with new configs
    cm_service.restart().wait()

    # execute the first run command
    print "Excuting first run command. This might take a while."
    cmd = cluster.first_run()

    while cmd.success == None:
        cmd = cmd.fetch()

    if cmd.success != True:
        print "The first run command failed: " + cmd.resultMessage()
        exit(0)

    print "First run successfully executed. Your cluster has been set up!"









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
  addSM(api)


if __name__ == "__main__":
  main()

