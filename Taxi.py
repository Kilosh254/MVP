# Import necessary libraries
from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Data storage for available taxis
available_taxis = [
            {"id": 1, "name": "Taxi 1", "available": True},
                {"id": 2, "name": "Taxi 2", "available": True},
                    # Add more taxis here
                    ]

# Data storage for booked rides
booked_rides = []

# API endpoint to list available taxis
@app.route('/taxis', methods=['GET'])
def get_available_taxis():
        return jsonify({"taxis": available_taxis})

    # API endpoint to book a taxi
    @app.route('/book', methods=['POST'])
    def book_taxi():
            data = request.get_json()

                # Find an available taxi
                    available_taxi = None
                        for taxi in available_taxis:
                                    if taxi["available"]:
                                                    available_taxi = taxi
                                                                break

                                                                if available_taxi:
                                                                            # Book the taxi
                                                                                    available_taxi["available"] = False
                                                                                            booked_rides.append({"taxi_id": available_taxi["id"], "passenger_name": data["passenger_name"]})
                                                                                                    return jsonify({"message": f"Taxi {available_taxi['id']} booked successfully!"})
                                                                                                    else:
                                                                                                                return jsonify({"message": "No available taxis."}), 400

                                                                                                            # API endpoint to list booked rides
                                                                                                            @app.route('/rides', methods=['GET'])
                                                                                                            def get_booked_rides():
                                                                                                                    return jsonify({"rides": booked_rides})

                                                                                                                if __name__ == '__main__':
                                                                                                                        app.run(debug=True)

