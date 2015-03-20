# rice/query.py
#
# Defines the Query class.
#

import urllib.request
import urllib.parse
import json
import os
from rice import error, util, package

class Query(object):
    def __init__(self, query):
      config_path = util.RDBDIR + "config"
      if os.path.exists(config_path) and os.path.isfile(config_path):
        with open(util.RDBDIR + "config") as config_file:
          try:
            config = json.load(config_file)
          except Exception as e:
            raise error.corruption_error("Invalid JSON: %s" %(e))
      else:
        config = dict()
        config["dbs"] = ["http://192.249.58.243:9000/"]
      try:
        query = urllib.parse.quote_plus(query)
        request = urllib.request.Request(config["dbs"][0] + query)
        response = urllib.request.urlopen(request).read().decode('utf-8')
      except Exception as e:
        raise error.Error("Could not connect to server %s: %s" % (config["dbs"], e))
      try:
        self.results = json.loads(response)
      except Exception as e:
        raise error.corruption_error("Could not read JSON from server: %s" %(e))

    def get_results(self):
      return [package.Package(i) for i in self.results]

