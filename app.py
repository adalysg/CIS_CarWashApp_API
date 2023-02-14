from flask import Flask
from flask_restful import Resource, Api, request
from car_wash_processor import CarWashDecisionProcessor
from noaa_interface import NoaaInterface

app = Flask(__name__)

api = Api(app)

class Decider(Resource):
    def get(self):
        noaa_interface = NoaaInterface()
        lat = request.args["lat"]
        long = request.args["long"]
        print(lat, long)
        car_processor = CarWashDecisionProcessor(lat, long, noaa_interface)
        return car_processor.do_wash()


# endpoints defined by "/"
# Think: '/carwashdecider' == home
api.add_resource(Decider, '/carwashdecider')

if __name__ == "__main__":
    app.run(debug=True)
