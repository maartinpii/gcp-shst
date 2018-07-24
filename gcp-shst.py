#!/bin/python

# Import pprint for process response
from pprint import pprint

# Import Google api client and auth
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from google.auth import compute_engine

# Import OS Lib for set env
import os

# Import parser for process command function
from argparse import ArgumentParser


# Instance Parser
parser = ArgumentParser(description='Script for auto start or shutdown GCP Env', prog='gcp-shst.py')
parser.add_argument('-p', '--project', dest='gcpProject', help='GCP CE project', metavar='GCP CE Project', required='true')
parser.add_argument('-z', '--zone', dest='gcpZone', help='GCP CE Zone', metavar='GCP CE Zone', required='true')
parser.add_argument('-i', '--instance', dest='gcpInst', help='GCP CE Name', metavar='GCP Instance Name', required='true')
parser.add_argument('-o', '--operation', dest='operation', help='Operation to execute (Start/Stop)', metavar='Action (start/stop)', required='true')


args = parser.parse_args()

# Set Environment Var for credentials
try:
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path4sc"
except:
  print("FAIL => Not possible to set App Credentials Env Var ")
  raise
  sys.exit(1)

# Set Credentials
credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Execute Request
try:
  if args.operation == 'start':
     request = service.instances().start(project=args.gcpProject, zone=args.gcpZone, instance=args.gcpInst)
     response = request.execute()
  elif args.operation == 'stop':  
     request = service.instances().stop(project=args.gcpProject, zone=args.gcpZone, instance=args.gcpInst)
     response = request.execute()

  else:
     print("FAIL => No operation selected ")
     sys.exit(1)
except Exception as e:
  raise
  sys.exit(1)

# TODO: Change code below to process the `response` dict:
pprint(response)
