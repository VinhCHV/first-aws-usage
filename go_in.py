import json


def start_phase(event, context):
    body = {
        "message": "Getting Started...",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
