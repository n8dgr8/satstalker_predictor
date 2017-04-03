from datetime import datetime
from pyorbital import orbital

tle_path = '/tmp/tle'
dsm_lat = 41.6005448
dsm_lon = -93.6091064
dsm_alt = 266.38

awesome_satellites = [
    'noaa 15',
    'noaa 18',
    'noaa 19'
]

def lambda_handler(event, context):

    # Save DSM Location (Lat / Lon)
    # Save DSM altitude
    # Get TLE file
    # Set up Orbitals for each satellite
    # Get now
    # foreach Orbital, get_next_passes for 24 hours

    now = datetime.utcnow()

    for satellite in awesome_satellites:
        sat_orbital = orbital.Orbital(satellite)

        print satellite
        print '-------'
        next_passes = sat_orbital.get_next_passes(now, 24, dsm_lon, dsm_lat, dsm_alt)

        for next_pass in next_passes:
            (start, end, max) = next_pass
            print '%02d:%02d:%02d' % (start.hour, start.minute, start.second)
            print '%02d:%02d:%02d' % (max.hour, max.minute, max.second)
            print '%02d:%02d:%02d' % (end.hour, end.minute, end.second)

def main():
    lambda_handler(None, None)

if __name__ == "__main__":
    main()
