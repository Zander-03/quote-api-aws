import json
import random
QUOTES = [
    
    "The best way to get started is to quit talking and begin doing.",
    "Don't let yesterday take up too much of today.",
    "It's not whether you get knocked down, it's whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are."
    ]
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'quote of the day': random.choice(QUOTES) }).encode('ascii', 'ignore').decode()
    }
