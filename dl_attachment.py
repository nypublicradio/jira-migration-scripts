import requests
import os

# grab this from an old-jira session after you've logged in
auth_cookie = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

s = requests.Session()
s.headers.update({'Cookie': auth_cookie})

with open('attachments.txt') as f:
    for url in f:
        image = url.rstrip()
        filepath = image.removeprefix('https://jira.wnyc.org/secure/attachment/') # python3.9 only
        try:
            folder, filename = filepath.split('/')
        except ValueError:
            vals = filepath.split('/')
            filename = vals[-1]
            folder = "/".join(vals[:-1])
        try:
            os.makedirs(os.path.join('attachments', folder), exist_ok=True)
        except:
            pass
        try:
            with open(os.path.join('attachments', folder, filename), 'wb') as img:
                r = s.get(image)
                img.write(r.content)
                print(f'saved {os.path.join("attachments", folder, filename)}')
        except OSError:
            print('could not upload', filename)
            pass
