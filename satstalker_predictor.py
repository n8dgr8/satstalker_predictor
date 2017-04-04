import json
from datetime import datetime

from pyorbital import orbital


def lambda_handler(event, context):
    tle_path = '/tmp/tle'

    now = datetime.utcnow()

    with open('./awesome_satellites.json') as file_data:
        awesome_satellites = json.load(file_data)

    for satellite in awesome_satellites:
        sat_orbital = orbital.Orbital(satellite['name'])

        print '%s @ %s' % (satellite['name'], satellite['frequency'])
        print '-------'
        next_passes = sat_orbital.get_next_passes(now, 24, event['lon'], event['lat'], event['alt'])

        for next_pass in next_passes:
            (start, end, maximum) = next_pass
            print '%02d:%02d:%02d' % (start.hour, start.minute, start.second)
            print '%02d:%02d:%02d' % (maximum.hour, maximum.minute, maximum.second)
            print '%02d:%02d:%02d' % (end.hour, end.minute, end.second)

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
