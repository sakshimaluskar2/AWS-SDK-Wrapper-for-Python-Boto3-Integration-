#In this file there is only functions
def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
       print(bucket.name)

#Uplod file from local to aws s3
#File handling = open , process,clode file
def uplode_file(s3_obj,bucket_name, file_path, key_name):
    file_data = open(file_path,'rb') #Open
    s3_obj.Bucket(bucket_name).put_object(Key=key_name,Body=file_data)#process
    file_data.close() #close
    print("File uploaded sucessfully")

def list_files(s3_obj, bucket_name):
    print(f"The files in{bucket_name}are:")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object)