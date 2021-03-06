import os
import boto3
import joblib
import pandas as pd

# download model file from S3 into /tmp folder
s3 = boto3.client('s3')
bucket = os.environ['BUCKET']
key = os.environ['KEY']
s3.download_file(bucket, key, '/tmp/model.pkl')
# LOAD MODEL
model = joblib.load('/tmp/model.pkl')


def handler(event, context):
    # TRANSFORM DATA
    data = pd.DataFrame(event, index=[0])
    # PREDICT
    prediction = float(model.predict(data))

    return {
        'lr': round(prediction, 2)
    }

