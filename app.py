from car_wash_processor import CarWashDecisionProcessor
from noaa_interface import NoaaInterface

def handler(event, context):
    # Logging
    print(f"Incoming event: {event}")

    noaa_interface = NoaaInterface()
    lat_long = event['rawQueryString']
    lat_long_dict = lat_long.split('&')
    lat_part, long_part = lat_long_dict[0], lat_long_dict[1]
    lat_val = lat_part.split("=")[1]
    long_val = long_part.split("=")[1]

    if not lat_val or not long_val:
        return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "Please provide lat and long."
    }
    car_processor = CarWashDecisionProcessor(lat_val, long_val, noaa_interface)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": car_processor.do_wash()
    }