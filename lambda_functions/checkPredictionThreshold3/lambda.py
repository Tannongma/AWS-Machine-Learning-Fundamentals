import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    # Handle the body if it’s a JSON string (as Step Function might pass it this way)
    if isinstance(event['body'], str):
        body = json.loads(event['body'])
    else:
        body = event['body'] 
    
    # Parse the inferences from string to list
    inferences_raw = body['inferences']
    if isinstance(inferences_raw, str):
        inferences = json.loads(inferences_raw)  # Convert string to list
    else:
        inferences = inferences_raw ## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(val > THRESHOLD for val in inferences) ## TODO: fill in
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }