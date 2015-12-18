#!/usr/bin/env python


from cm_api.api_client import ApiResource, ApiException


def main():
  print 'create HDD cluster'
  api = ApiResource('r2341-d5-us01.dssd.com', 'admin', 'admin')
  api.create_cluster(name="HDDTest", version="CDH5")
  sleep(10)



if __name__=='__main__':
  main()
  
