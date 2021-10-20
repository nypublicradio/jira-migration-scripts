import boto3
import os

s3 = boto3.client('s3')

os.chdir('attachments')
for d in os.listdir():
    for f in os.listdir(d):
        filepath = os.path.join(d, f)
        with open(filepath, 'rb') as upload:
            s3.upload_fileobj(upload, 'nypr-jira-attachments', filepath)
            print(f'uploaded {filepath}')
