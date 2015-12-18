#!/usr/bin/env python


#add cloudera manager service
#https://github.com/cloudera/cm_api/blob/master/python/examples/auto-deploy/deploycloudera.py




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

FIREHOSE_DATABASE_PASSWORD="Uq0Wz7kksX"
HEADLAMP_DATABASE_PASSWORD="vSVFkQwRRp"
CM_HOST='r2341-d5-us01.dssd.com'

# without the roles we end up with MGMT which cant start
AMON_ROLENAME="ACTIVITYMONITOR"
AMON_ROLE_CONFIG = {
   'firehose_database_host': "r2341-d5-us01.dssd.com:7432",
   'firehose_database_user': 'amon',
   'firehose_database_password': FIREHOSE_DATABASE_PASSWORD,
   'firehose_database_type': 'postgresql',
   'firehose_database_name': 'amon',
   'firehose_heapsize': '215964392',
}
APUB_ROLENAME = "ALERTPUBLISHER" 
APUB_ROLE_CONFIG = { }
ESERV_ROLENAME = "EVENTSERVER"
ESERV_ROLE_CONFIG = {
   'event_server_heapsize': '215964392'
}
HMON_ROLENAME = "HOSTMONITOR"
HMON_ROLE_CONFIG = {u'firehose_heapsize': u'268435456', u'firehose_non_java_memory_bytes': u'1610612736'}
SMON_ROLENAME = "SERVICEMONITOR"
SMON_ROLE_CONFIG = {u'firehose_heapsize': u'268435456', u'firehose_non_java_memory_bytes': u'1610612736' }
RMAN_ROLENAME = "REPORTMANAGER"
RMAN_ROLE_CONFIG = {
   'headlamp_database_host': "r2341-d5-us01.dssd.com:7432",
   'headlamp_database_user': 'rman',
   'headlamp_database_password': HEADLAMP_DATABASE_PASSWORD,
   'headlamp_database_type': 'postgresql',
   'headlamp_database_name': 'rman',
   'headlamp_heapsize': '215964392',
}
MGMT_SERVICENAME="MGMT"
MGMT_SERVICE_CONFIG={}
MGMT_ROLE_CONFIG={}


  

def deploy_management(manager, mgmt_servicename, mgmt_service_conf, mgmt_role_conf, amon_role_name, amon_role_conf, apub_role_name, apub_role_conf, eserv_role_name, eserv_role_conf, hmon_role_name, hmon_role_conf, smon_role_name, smon_role_conf, rman_role_name, rman_role_conf):
   #mgmt = manager.create_mgmt_service(ApiServiceSetupInfo())
   print "getting mgmt service object"
   mgmt_service = manager.get_service()
   
   print "before autoconfgiure:"
   for group in mgmt_service.get_all_role_config_groups():
     print "group:", group
     print "group_config:", group.get_config()



   # create roles. Note that host id may be different from host name (especially in CM 5). Look it it up in /api/v5/hosts
   #mgmt_service.create_role(amon_role_name + "-1", "ACTIVITYMONITOR", CM_HOST)
   #mgmt_service.create_role(apub_role_name + "-1", "ALERTPUBLISHER", CM_HOST)
   #mgmt_service.create_role(eserv_role_name + "-1", "EVENTSERVER", CM_HOST)
   #mgmt_service.create_role(hmon_role_name + "-1", "HOSTMONITOR", CM_HOST)
   #mgmt_service.create_role(smon_role_name + "-1", "SERVICEMONITOR", CM_HOST)
   ##mgmt.create_role(nav_role_name + "-1", "NAVIGATOR", CM_HOST)
   ##mgmt.create_role(navms_role_name + "-1", "NAVIGATORMETADATASERVER", CM_HOST)
   ##mgmt.create_role(rman_role_name + "-1", "REPORTSMANAGER", CM_HOST)
   
   # now configure each role   
 #  for group in mgmt_service.get_all_role_config_groups():
 #      if group.roleType == "ACTIVITYMONITOR":
 #          group.update_config(amon_role_conf)
 #      elif group.roleType == "ALERTPUBLISHER":
 #          group.update_config(apub_role_conf)
 #      elif group.roleType == "EVENTSERVER":
 #          group.update_config(eserv_role_conf)
 #      elif group.roleType == "HOSTMONITOR":
 #          group.update_config(hmon_role_conf)
 #      elif group.roleType == "SERVICEMONITOR":
 #          group.update_config(smon_role_conf)
   # #   elif group.roleType == "NAVIGATOR":
   # #       group.update_config(nav_role_conf)
   # #   elif group.roleType == "NAVIGATORMETADATASERVER":
   # #       group.update_config(navms_role_conf)
   # #   elif group.roleType == "REPORTSMANAGER":
   # #       group.update_config(rman_role_conf)
   
   # now start the management service
   #manager.auto_assign_roles()
   #manager.auto_configure()
   print "after autoconfigure:"

   for group in mgmt_service.get_all_role_config_groups():
     print "group:", group
     print "group_config:", group.get_config()



   mgmt_service.start().wait()
   
   return mgmt_service



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
  print "host connected, getting cloudera manager "
  MANAGER = api.get_cloudera_manager()
  print "have cloudera manager object" 
  deploy_management(MANAGER, MGMT_SERVICENAME, MGMT_SERVICE_CONFIG, MGMT_ROLE_CONFIG, AMON_ROLENAME, AMON_ROLE_CONFIG, APUB_ROLENAME, APUB_ROLE_CONFIG, ESERV_ROLENAME, ESERV_ROLE_CONFIG, HMON_ROLENAME, HMON_ROLE_CONFIG, SMON_ROLENAME, SMON_ROLE_CONFIG, RMAN_ROLENAME, RMAN_ROLE_CONFIG)
  print "Deployed CM management service " + MGMT_SERVICENAME + " to run on " + CM_HOST

if __name__ == "__main__":
  main()

