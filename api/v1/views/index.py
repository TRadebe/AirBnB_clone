#!/usr/bin/python3
'''Index API View'''

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the API status.

    Returns:
        JSON: Status information with the key 'status' set to 'OK'.
    """
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat():
    """
    Returns statistics about the number of each object type.

    Returns:
        JSON: Object counts for amenities, cities, places, reviews, states, and users.
    """
    return jsonify(
        amenities=storage.count('Amenity'),
        cities=storage.count('City'),
        places=storage.count('Place'),
        reviews=storage.count('Review'),
        states=storage.count('State'),
        users=storage.count('User')
    )
