#In this files there is only calls 
import boto3
from aws_wrapper import show_buckets,uplode_file,list_files

s3_obj = boto3.resource('s3')

file_path='day_9\my_test_uplode_file.txt'
show_buckets(s3_obj)
#uplode_file(s3_obj,'pfd-batch2-sakshi',file_path,'my_test_uplode_file.txt')

list_files(s3_obj,'pfd-batch2-sakshi')