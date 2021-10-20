import csv
import sys
# jira dumps break csv field limit (131072 default for me)
csv.field_size_limit(999999)

try:
    proj = str.upper(sys.argv[1])
except:
    sys.exit("please give project key as arg")

# Copied, pasted, easier than calculating here
HEADER = "Set as ToDo Status (Ready for Dev?),Assignee,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Attachment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Comment,Created,Capital Expenditure (CapEx) Hours,Developer,Epic Color,Epic Link,Epic Name,Epic Status,Flagged,Rank,Story Points,Description,Fix Version/s,Fix Version/s,Fix Version/s,Fix Version/s,Fix Version/s,Fix Version/s,Fix Version/s,Fix Version/s,Issue Type,Issue id,Issue key,Labels,Labels,Labels,Labels,Labels,Labels,Labels,Labels,Outward issue link (Blocks),Outward issue link (Blocks),Outward issue link (Blocks),Outward issue link (Blocks),Outward issue link (Cloners),Outward issue link (Duplicate),Outward issue link (Duplicate),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Outward issue link (Relates),Parent id,Priority,Reporter,Resolution,Resolved,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Sprint,Status,Summary"

proj_tix = []
processed_tix_file = 's3-attachments-normalized-jira-tix.csv'

with open(processed_tix_file) as f:
    tickets = csv.reader(f)
    ticket_index = 259 #MAGIC NUMBER -- this col in csv has issue key
    for ticket in tickets:
        issue_key = ticket[ticket_index]
        project = issue_key.split('-')[0]
        if project == proj:
            proj_tix.append(ticket)

with open(f'{proj}-processed-tix.csv', 'w') as f:
    f.write(HEADER)
    f.write("\n")
    writer = csv.writer(f)
    for ticket in proj_tix:
        writer.writerow(ticket)


