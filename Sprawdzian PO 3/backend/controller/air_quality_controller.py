from flask import Blueprint, request, jsonify
from backend.services.air_quality_service import AirQualityService

air_quality_blueprint = Blueprint('air_quality', __name__)
service = AirQualityService()

@air_quality_blueprint.route('/air_quality', methods=['POST'])
def add_air_quality_data():
    data = request.json
    try:
        service.add_air_quality_data(data)
        return jsonify({"message": "Data added successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@air_quality_blueprint.route('/air_quality/nearest', methods=['GET'])
def get_nearest_air_quality_data():
    timestamp = request.args.get('timestamp')
    if not timestamp:
        return jsonify({"error": "Timestamp is required"}), 400
    data = service.get_nearest_air_quality_data(timestamp)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No data found"}), 404
