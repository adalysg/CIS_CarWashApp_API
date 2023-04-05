from car_wash_processor import CarWashDecisionProcessor
from noaa_interface import NoaaInterface

def handler(event, context):
    # Logging
    print(f"Incoming event: {event}")

    noaa_interface = NoaaInterface()
    lat = event.get("lat")
    long = event.get("long")

    if not lat or not long:
        return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "Please provide lat and long."
    }
    car_processor = CarWashDecisionProcessor(lat, long, noaa_interface)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": car_processor.do_wash()
    }