#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Originally adapted from timeseries.py as part of the cm_api module
#
#     https://github.com/cloudera/cm_api/blob/cm-4.6/python/examples/timeseries.py

"""
Interact with Cloudera Manager

Usage: %s [options]

Options:
-h --help                          Show help
--host=<cm-server-host>            Specify a Cloudera Manager Server host
                                   Defaults to 'localhost'
--port=<cm-server-port>            Override the default Cloudera Manager Server port
                                   Defaults to '7180'
--version=<cm-server-api-version>  Define the Cloudera Manager Server API version
                                   Defaults to latest as defined in the cm_api python module
--user=<cm-server-user>            The Cloudera Manager user
                                   Defaults to 'admin'
--user=<cm-server-user-password>   The Cloudera Manager user password
                                   Defaults to 'admin'
                                   
"""

from cm_api import api_client
from cm_api.api_client import ApiResource
import getopt
import inspect
import logging
import sys
import textwrap

LOG = logging.getLogger(__name__)

def do_work(host, port, version, user, password):
    ApiResource(host, port, user, password, False, version)
    print "DO SOME WORK WITH THE CM API"

def usage():
    doc = inspect.getmodule(usage).__doc__
    print >> sys.stderr, textwrap.dedent(doc % (sys.argv[0],))

def setup_logging(level):
    logging.basicConfig()
    logging.getLogger().setLevel(level)

def main(argv):
    setup_logging(logging.INFO)

    host = 'localhost'
    port = 7180
    version = api_client.API_CURRENT_VERSION
    user = 'admin'
    password = 'admin'    

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "host=", "port=", "version=", "user=", "password="])
    except getopt.GetoptError, err:
        print >> sys.stderr, err
        usage()
        return -1

    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            return -1
        elif option in ("--host"):
            host = value;
        elif option in ("--port"):
            port = value;
        elif option in ("--version"):
            version = value;
        elif option in ("--user"):
            user = value;
        elif option in ("--password"):
            password = value;
        else:
            print >> sys.stderr, "Unknown flag: ", option
            return -1

    if args:
        do_work(host, port, version, user, password)
        return 0
    else:
        usage()
        return -1

if __name__ == '__main__':
    sys.exit(main(sys.argv))
