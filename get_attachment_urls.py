import csv

def list_attachments(project=None):
    # jira dumps break csv field limit (131072 default for me)
    csv.field_size_limit(999999)


    with open(f'./normalized-jira-tix.csv') as f:
        tickets = csv.reader(f)
        for ticket in tickets:
            issue_key = ticket[259]
            proj = issue_key.split('-')[0]
            if project is None or proj == project:
                for field in ticket:
                    if 'https://jira.wnyc.org/secure/attachment' in field:
                        print(field.split(';')[-1])
                
list_attachments()
