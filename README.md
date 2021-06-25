# aws_emr_spark_terraform
This Repo consists of a demo with terraform files to automate S3 data processing with Spark
The demo will be divided into 2 parts:
a) Ingest a file from S3 and transform it using pyspark and load it in a csv on S3
b) Ingest a file from S3 and transform it and load it into Redshift

Steps Involved are:
a) Create an EMR cluster with 2 worker nodes
b) Deploy code and files to S3 through terraform
c) Submit the Spark Job
d) Terminate the EMR cluster 
