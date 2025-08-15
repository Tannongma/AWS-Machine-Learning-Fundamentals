import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = "test/bicycle_s_000513.png" ## TODO: fill in

    ## TODO: fill in
    #boto_session = boto3.session.Session()
    #bucket =  sagemaker.session.generate_default_sagemaker_bucket_name(boto_session)
    bucket = "sagemaker-us-east-1-586794439862"
    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    bucket_name = bucket
    s3_file_key = key  # S3 object key
    local_file_path = "/tmp/image.png"  # Local file path

    # Download the file
    try:
        s3.download_file(bucket_name, s3_file_key, local_file_path)
        print(f"File downloaded successfully to {local_file_path}")
    except Exception as e:
        print(f"Error occurred: {e}")
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }