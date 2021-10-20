import requests
import os

# grab this from an old-jira session after you've logged in
auth_cookie = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

s = requests.Session()
s.headers.update({'Cookie': auth_cookie})

api = 'https://jira.wnyc.org/sr/jira.issueviews:searchrequest-csv-all-fields/temp/SearchRequest.csv?jqlQuery=&delimiter=,&tempMax=1000&pager/start='

totaltix = 20495 # this can be found several places, including 
  # https://jira.wnyc.org/secure/migration-app-action.jspa#/home
  # Be sure to update before running
idx = 0
try:
    os.mkdir('jiratix')
except:
    pass

while idx < totaltix:
    r = s.get(api + str(idx))
    print(f"downloaded from index {idx} -- response {r.status_code}")
    with open(f'jiratix/jira-tix-{idx}.csv', 'w') as f:
        f.write(r.text)
    idx += 1000
