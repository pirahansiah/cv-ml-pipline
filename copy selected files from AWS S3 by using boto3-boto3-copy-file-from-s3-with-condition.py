# Farshid PirahanSiah 17 March 2020
# copy selected files from AWS S3 by using boto3
# You can set two variables :
    # number_of_files_to_escape
    # how_many_files_you_need

# # !/usr/local/bin/python3

import boto3
from botocore.exceptions import ClientError
def get_all_s3_objects(s3, **base_kwargs):
    continuation_token = None
    while True:
        list_kwargs = dict(MaxKeys=1000000, **base_kwargs)
        if continuation_token:
            list_kwargs['ContinuationToken'] = continuation_token
        response = s3.list_objects_v2(**list_kwargs)
        yield from response.get('Contents', [])
        if not response.get('IsTruncated'):
            break
        continuation_token = response.get('NextContinuationToken')
def main():
    bucket = 'sagemaker-us-east-1'
    prefix = 'images/'
    number_of_files_to_escape=0
    s3=boto3.client('s3')
    how_many_files_you_need=0
    for file in get_all_s3_objects(boto3.client('s3'), Bucket=bucket, Prefix=prefix):
        number_of_files_to_escape=number_of_files_to_escape+1
        if (number_of_files_to_escape>40):
            number_of_files_to_escape=0
            print("> %s/%s" % (bucket, file['Key']))
            fileName=file['Key']
            if (not fileName.endswith('.png.')):
                strFile='/Users/farshid/'+str(how_many_files_you_need)+'.png' 
                s3.download_file(bucket, file['Key'], strFile)
                how_many_files_you_need=how_many_files_you_need+1
                if (how_many_files_you_need>110):
                    break
if __name__ == '__main__':
    main()
