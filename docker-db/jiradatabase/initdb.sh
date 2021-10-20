#!/bin/bash
psql -U docker <<-EOSQL
    \connect jira
    \i crazy_jira_header.sql
    COPY jira FROM '/s3-attachments-normalized-jira-tix.csv' DELIMITER ',' CSV HEADER;
EOSQL
