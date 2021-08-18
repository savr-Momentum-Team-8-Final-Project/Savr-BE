import os
import logging
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import numpy as np
import urllib
import cv2

s3_signature ={
'v4':'s3v4',
'v2':'s3'
}



def create_presigned_url(bucket_name, bucket_key, expiration=3600, signature_version=s3_signature['v4']):

    s3_client = boto3.client('s3',
                         aws_access_key_id="AWS_ACCESS_KEY",
                         aws_secret_access_key="AWS_SECRET_ACCESS_KEY",
                         config=Config(signature_version=signature_version),
                         region_name='ap-south-1'
                         )
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                Params={'Bucket': bucket_name,
                                                        'Key': bucket_key},
                                                ExpiresIn=expiration)
        print(s3_client.list_buckets()['Owner'])
        for key in s3_client.list_objects(Bucket=bucket_name,Prefix=bucket_key)['Contents']:
            print(key['Key'])
    except ClientError as e:
        logging.error(e)
        return None
        # The response contains the presigned URL
    return response

def url_to_image(URL):
    ### ??????
    resp = urllib.request.urlopen('https://savrbeteam.s3.amazonaws.com/media/r10_jrQJ8kn.png')
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image


seven_days_as_seconds = 604800

generated_signed_url = create_presigned_url(you_bucket_name, bucket_key, 
seven_days_as_seconds, s3_signature['v4'])
print(generated_signed_url)
image_complete = url_to_image(generated_signed_url)

#just debugging Purpose to show the read Image
cv2.imshow('Final_Image',image_complete)
cv2.waitKey(0)
cv2.destroyAllWindows()

### Use For Loop to iterate to all Keys In The KeyList. Just Before calling the Function create_presigned_url.