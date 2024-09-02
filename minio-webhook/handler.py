import sys
import json

def handle(event, context):
    # Read the incoming webhook data
    try:
        # Convert the event body to a dictionary
        event_data = json.loads(event.body)

        # Process the event (e.g., log the event, extract information, etc.)
        print("Received MinIO event:", event_data)
        
        return {
            "statusCode": 200,
            "body": "Webhook processed successfully"
        }

    except Exception as e:
        print("Error processing webhook:", str(e))
        return {
            "statusCode": 500,
            "body": "Failed to process webhook"
        }

if __name__ == "__main__":
    # For local testing, read from standard input
    event = type('Event', (object,), {'body': sys.stdin.read()})()
    result = handle(event, None)
    print(result)
