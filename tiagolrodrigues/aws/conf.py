import datetime
import os
'''
#AWS_ACCESS_KEY_ID = 'AKIAZUXWJUSKYQAA6RCH'#os.environ.get('nba_akid')
#AWS_SECRET_ACCESS_KEY = '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'#os.environ.get('nba_sak')
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

#DEFAULT_FILE_STORAGE = 'nailsbyannie.aws.utils.MediaRootS3BotoStorage'
#STATICFILES_STORAGE = 'nailsbyannie.aws.utils.StaticRootS3BotoStorage'
#AWS_STORAGE_BUCKET_NAME = 'nailsbyannie'#os.environ.get('nba_bucket')
S3DIRECT_REGION = 'us-east-2'
#S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
#STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
#AWS_DEFAULT_ACL = 'public-read'
#AWS_S3_REGION_NAME = 'us-east-2'


two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}'''

AWS_ACCESS_KEY_ID = os.environ.get('tlr_akid')
AWS_SECRET_ACCESS_KEY = os.environ.get('tlr_sak')
AWS_STORAGE_BUCKET_NAME = os.environ.get('tlr_bucket')
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'tiagolrodrigues.aws.utils.MediaRootS3BotoStorage'
#STATICFILES_STORAGE = 'nailsbyannie.aws.utils.StaticRootS3BotoStorage'
#STATIC_URL = 'https://{}.s3.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME)
#ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_HOST = "s3.us-east-2.amazonaws.com"
MEDIA_URL = 'https://{}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_ROOT = MEDIA_URL
