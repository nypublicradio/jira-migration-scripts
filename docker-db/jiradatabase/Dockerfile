FROM postgres:9.6.21
# ENV POSTGRES_PASSWORD=jirapass
EXPOSE 5432
COPY crazy_jira_header.sql /
COPY s3-attachments-normalized-jira-tix.csv /
COPY initdb.sh /

ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB docker
ADD crazy_jira_header.sql /docker-entrypoint-initdb.d/
ADD initdb.sh /docker-entrypoint-initdb.d/
