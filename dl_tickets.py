import os
import requests
import sys

# grab this from an old-jira session after you've logged in
auth_cookie = ''#TODO: INSERT YOUR ACTUAL COOKIE
if not auth_cookie:
    sys.exit("You must add your auth cookie to the script")

s = requests.Session()
s.headers.update({'Cookie': auth_cookie})

api = 'https://jira.wnyc.org/sr/jira.issueviews:searchrequest-csv-all-fields/temp/SearchRequest.csv?jqlQuery=&delimiter=,&tempMax=1000&pager/start='
api2 = 'https://jira.wnyc.org/sr/jira.issueviews:searchrequest-csv-all-fields/temp/SearchRequest.csv?jqlQuery=project%20%3D%20"Broadcast%20Apps"%20ORDER%20BY%20created%20ASC&delimiter=,&tempMax=1000&pager/start='

totaltix = 20519 # this can be found several places, including 
  # https://jira.wnyc.org/secure/migration-app-action.jspa#/home
  # Be sure to update before running
idx = 0
try:
    os.mkdir('jiratix')
except:
    pass

while idx < totaltix:
    r = s.get(api2 + str(idx))
    print(f"downloaded from index {idx} -- response {r.status_code}")
    with open(f'jiratix/broad-tix-{idx}.csv', 'w') as f:
        f.write(r.text)
    idx += 1000
