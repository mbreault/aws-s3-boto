import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name):
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
