import collections
import csv
import os
from urllib import parse

critical_fields = {
    "Assignee": "Assignee",
    "Attachment": "Attachment",
    "Custom field (Capital Expenditure (CapEx) Hours)": "Capital Expenditure (CapEx) Hours",
    "Comment": "Comment",
    "Created": "Created",
    "Description": "Description",
    "Custom field (Developer)": "Developer",
    "Custom field (Epic Colour)": "Epic Color",
    "Custom field (Epic Link)": "Epic Link",
    "Custom field (Epic Name)": "Epic Name",
    "Custom field (Epic Status)": "Epic Status",
    "Fix Version/s": "Fix Version/s",
    "Custom field (Flagged)": "Flagged",
    "Issue id": "Issue id",
    "Issue key": "Issue key",
    "Issue Type": "Issue Type",
    "Labels": "Labels",
    "Outward issue link (Blocks)": "Outward issue link (Blocks)",
    "Outward issue link (Cloners)": "Outward issue link (Cloners)",
    "Outward issue link (Duplicate)": "Outward issue link (Duplicate)",
    "Outward issue link (Relates)": "Outward issue link (Relates)",
    "Parent id": "Parent id",
    "Priority": "Priority",
    "Custom field (Rank)": "Rank",
    "Reporter": "Reporter",
    "Resolution": "Resolution",
    "Resolved": "Resolved",
    '"Custom field (Set to ""To Do"" Status (Ready for active development/work)?)"': 'Set as ToDo Status (Ready for Dev?)',
    "Sprint": "Sprint",
    "Status": "Status",
    "Custom field (Story Points)": "Story Points",
    "Summary": "Summary"
}

old_field_to_new = dict((v,k) for k,v in critical_fields.items())

class Counts:
    max_counts = None

    def get_max_counts():
        if Counts.max_counts == None:
            Counts.max_counts = Counts._calculate_header_counts()
        return Counts.max_counts

    def _calculate_header_counts():
        max_counts = collections.Counter()
        csvs = os.listdir('jiratix')
        for tickets_dump in csvs:
            my_counts = collections.Counter()
            with open(f'./jiratix/{tickets_dump}') as f:
                headers = str.strip(f.readline())
            for header in headers.split(','):
                my_counts[header] += 1
            max_counts = max_counts | my_counts
        return max_counts 

class Issue:
    def __init__(self):
        self.data = {}
        for field, count in Counts.get_max_counts().items():
            self.data[field] = [''] * count

    def add_field(self, header, field):
        # id like to use a generator here but not gonna take the 
        # code complexity hit -- for this throwaway script i'll 
        # take the time complexity hit in exchange 

        # for i in range(len(self.data[header])):
        #     if self.data[header][i] == "":
        #         self.data[header][i] = field
        #         break
        self.data[header].insert(0,field)
        self.data[header].pop()

    def to_csv_as_list(self):
        output = []
        for k in sorted(critical_fields.keys()): # be sure to sort!!!
            if k == "Comment":
                output += self.data[k]
                # import pdb; pdb.set_trace()
                # output += reversed(self.data[k]) # comments will be ingested in reverse order
            elif k == "Attachment":
                escpd_attchmnts = []
                for attachment in self.data[k]:
                    # here goes, some uply code
                    splt_fields = attachment.split(';')
                    parsed_url = parse.urlparse(splt_fields[-1])
                    newurl = parsed_url._replace(path=parse.quote(parsed_url.path)).geturl()
                    # print(newurl)
                    splt_fields[-1] = newurl
                    escpd_attchmnts.append(';'.join(splt_fields))
                output += escpd_attchmnts
            else:
                output += self.data[k]
        return output


    def std_header():
        """
        abc sorted csv header with correct number of fields
        """
        header_counts = Counts.get_max_counts()
        csvheader = ""
        for k in sorted(critical_fields.keys()): # be sure to sort!!!
            # csvheader += f'{critical_fields[k]},' * header_counts[k]
            for n in range(header_counts[k]):
                csvheader += f'{critical_fields[k]}{n},'
        return csvheader.rstrip(',')

def consume_files():
    csv.field_size_limit(999999)
    csvs = os.listdir('jiratix')
    issues = []
    for tickets_dump in csvs:
    # for tickets_dump in ['jira-tix-1000.csv']:
        with open(f'./jiratix/{tickets_dump}') as f:
            special_header = str.strip(f.readline())
            headers_array = special_header.split(',')
            tickets = csv.reader(f)
            # import pdb; pdb.set_trace()
            for ticket in tickets:
                issue = Issue()
                for idx, field in enumerate(ticket):
                    hdr = headers_array[idx]
                    issue.add_field(hdr, field)
                issues.append(issue)
    return issues

def write_output_csv(ticket_corpus):
    with open('normalized-jira-tix.csv', 'w') as f:
        f.write(Issue.std_header())
        f.write('\n')
        writer = csv.writer(f)
        for t in ticket_corpus:
            writer.writerow(t.to_csv_as_list())


ticket_corpus = consume_files()
# import pdb; pdb.set_trace()
write_output_csv(ticket_corpus)
