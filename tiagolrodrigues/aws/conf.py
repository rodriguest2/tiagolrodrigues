import datetime
import os


AWS_ACCESS_KEY_ID = os.environ.get('tlr_akid')
AWS_SECRET_ACCESS_KEY = os.environ.get('tlr_sak')
AWS_STORAGE_BUCKET_NAME = os.environ.get('tlr_bucket')
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'tiagolrodrigues.aws.utils.MediaRootS3BotoStorage'
AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_HOST = "s3.us-east-2.amazonaws.com"
MEDIA_URL = 'https://{}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_ROOT = MEDIA_URL
