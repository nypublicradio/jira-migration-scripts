Preliminary Steps:
  1. Download tix with `dl_tickets.py`
     a. Gives `jiratix` dir
  2. Fix up the data with `issue_normalizer.py`
     a. Gives `normalized-jira-tix.csv`, containing all tix for all projects
  3. Deal with attachments
     a. i did this already, but the download and upload scripts are available
        - dl_attachment.py
	- ul_attachment.py
	i. `dl_attachment` requires `attachments.txt`
	ii. `ul_attachment` requires `attachments/` dir
	iii. you can get the `attachments.txt` with `get_attachment_urls.py > attachments.txt`
	iv. dl_attachment will generate `attachments/` 
     b. these attachments are hosted PUBLICLY in s3://nypr-jira-attachments
     c. you can replace the atlassian urls with the s3 urls by using the sed
        snippet in `attachment-url-sed-replace.sh`
	i. this creates the final form of the tickets csv: 
	   `s3-attachments-normalized-jira-tix.csv'
	ii. this is the best one to use generally, say for viewing in excel/numbers

Jira Cloud Import:
  (assuming you have `s3-attachments-normalized-jira-tix.csv` generated)

  1. Collate the tickets for a given project (where PROJ_PREFIX is like 'devo' or 'goth'):
    `python3 filter_tix.py $PROJ_PREFIX`
     
     -- the resulting file, `{PROJ_PREFIX}-processed-tix.csv` can be uploaded to 
        cloud jira.

  2. in cloud jira, you can choose to "reuse" a previous options configuration.
     use `CSV-configuration-202109281904.txt` for this.


Docker DB/API:
  There exists a possiblity that it is not worth using jira cloud to host
  historic tickets. If hosted cloud is axed, this could be a fair solution
  for maintaining an archive of pre-jira cloud tickets.

  1. cd to the docker-db dir
  2. run docker-compose up

  you should have available a sql database of all tickets and a rudimentary
  api to access arbitrary tickets. it could easily be grown into a robust
  ticket browser, depending on need.
