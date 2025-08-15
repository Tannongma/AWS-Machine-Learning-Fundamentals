import json
#import sagemaker
import boto3
import base64
#from sagemaker.serializers import IdentitySerializer


# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2025-07-28-12-37-23-199" ## TODO: fill in

def lambda_handler(event, context):

    # Decode the image data

    # Handle the body if it’s a JSON string (as Step Function might pass it this way)
    if isinstance(event['body'], str):
        body = json.loads(event['body'])
    else:
        body = event['body']

    image_data = body['image_data']
    
    image = base64.b64decode(image_data)

    # Instantiate a Predictor


    #predictor = sagemaker.predictor.Predictor(endpoint_name=ENDPOINT) ## TODO: fill in
    prediction = boto3.client('runtime.sagemaker').invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="image/png",
        Body=image
    )

    # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    #payload = image
    #inferences = predictor.predict(payload) ## TODO: fill in
    inferences = prediction['Body'].read() ## TODO: fill in
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }