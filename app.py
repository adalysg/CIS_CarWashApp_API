from car_wash_processor import CarWashDecisionProcessor
from noaa_interface import NoaaInterface

def handler(event, context):
    # Logging
    print(f"Incoming event: {event}")

    noaa_interface = NoaaInterface()
    lat_long = event['rawQueryString']
    lat_long_dict = lat_long.split('&')
    lat_part, long_part = lat_long_dict[0], lat_long_dict[1]
    lat_val = int(lat_part.split("=")[1])
    long_val = int(long_part.split("=")[1])

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

event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '/', 'rawQueryString': 'lat=undefined&long=undefined', 'headers': {'x-amzn-lambda-proxying-cell': '0', 'content-length': '0', 'x-amzn-tls-version': 'TLSv1.2', 'accept-language': 'en-US,en;q=0.9', 'x-forwarded-proto': 'https', 'x-forwarded-port': '443', 'x-forwarded-for': '2603:9001:a101:bfe5:a91f:24aa:bd3c:899b', 'x-amzn-lambda-proxy-auth': 'HmacSHA256, SignedHeaders=x-amzn-lambda-forwarded-client-ip;x-amzn-lambda-forwarded-host;x-amzn-lambda-proxying-cell, Signature=IiEicpY2Cgei1quj8vEZr56uZuZpHIoCaqcin2xXPes=', 'accept': '*/*', 'x-amzn-lambda-forwarded-client-ip': '2603:9001:a101:bfe5:a91f:24aa:bd3c:899b', 'x-amzn-tls-cipher-suite': 'ECDHE-RSA-AES128-GCM-SHA256', 'x-amzn-trace-id': 'Self=1-6436dec8-7c949dea2c93e6eb7bebfb92;Root=1-6436dec8-61b36d8301b0bc0d49913922', 'host': 'yayw3a47malmotovh5isklmvly0pyvaj.cell-1-lambda-url.us-east-1.on.aws', 'x-amzn-lambda-forwarded-host': 'yayw3a47malmotovh5isklmvly0pyvaj.lambda-url.us-east-1.on.aws', 'accept-encoding': 'gzip, deflate, br', 'user-agent': 'Expo/2.28.7.1017523 CFNetwork/1406.0.4 Darwin/22.3.0'}, 'queryStringParameters': {'lat': 'undefined', 'long': 'undefined'}, 'requestContext': {'accountId': 'anonymous', 'apiId': 'yayw3a47malmotovh5isklmvly0pyvaj', 'domainName': 'yayw3a47malmotovh5isklmvly0pyvaj.cell-1-lambda-url.us-east-1.on.aws', 'domainPrefix': 'yayw3a47malmotovh5isklmvly0pyvaj', 'http': {'method': 'GET', 'path': '/', 'protocol': 'HTTP/1.1', 'sourceIp': '2603:9001:a101:bfe5:a91f:24aa:bd3c:899b', 'userAgent': 'Expo/2.28.7.1017523 CFNetwork/1406.0.4 Darwin/22.3.0'}, 'requestId': 'e0535af5-ae15-464f-943b-5729aa78fcb1', 'routeKey': '$default', 'stage': '$default', 'time': '12/Apr/2023:16:39:36 +0000', 'timeEpoch': 1681317576333}, 'isBase64Encoded': False}

response = handler(event, "")

print(response)