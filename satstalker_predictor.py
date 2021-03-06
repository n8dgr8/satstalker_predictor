import json
from datetime import datetime

import boto3
from pyorbital import orbital, tlefile


def publish_sqs(message):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='satstalker_predictor')
    response = queue.send_message(MessageBody=json.dumps(message))
    print response

def publish_sns(message):
    sns = boto3.resource('sns')

    topic = sns.Topic('arn:aws:sns:us-east-1:406316711618:satstalker-predictor')

    response = topic.publish(
        Message=json.dumps(message)
    )

    print response

def lambda_handler(event, context):
    tle_path = '/tmp/tle'

    now = datetime.utcnow()

    with open('./awesome_satellites.json') as file_data:
        awesome_satellites = json.load(file_data)

    tlefile.fetch(tle_path)

    for satellite in awesome_satellites:
        sat_orbital = orbital.Orbital(satellite['name'], tle_file=tle_path)

        next_passes = sat_orbital.get_next_passes(now, 24, event['lon'], event['lat'], event['alt'])

        for next_pass in next_passes:
            (start, end, maximum) = next_pass

            publish_sns(
                {
                    'satellite': satellite,
                    'pass_begin': start.isoformat(),
                    'pass_end': end.isoformat()
                }
            )

def main():
    dsm_lat = 41.6005448
    dsm_lon = -93.6091064
    dsm_alt = 266.38

    lambda_handler(
        {
            'lon': dsm_lon,
            'lat': dsm_lat,
            'alt': dsm_alt
        },
        None
    )

if __name__ == "__main__":
    main()
