#!/usr/bin/env python


import logging
from cm_api.api_client import ApiResource

LOG=logging.getLogger(__name__)

def setup_logging(level):
  logging.basicConfig()
  logging.getLogger().setLevel(level)


class ImpalaQuery(object):
  """
  """
  try:
    opts, args - getopt.getopt(argv[1:],"hf:t") 
  except getopt.GetoptError, err:
    #print >>sys.stderr, err
    #return -1



def main(argv):
  setup_logging(logging.INFO)


if __name__ == '__main__:
   sys.exit(main(sys.argv))
