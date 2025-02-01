import json


def end_phase(event, context):
    body = {
        "message": "Ending_phase",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
