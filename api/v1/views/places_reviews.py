#!/usr/bin/python3
'''Places Reviews API View'''

from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def review(place_id):
    """
    Retrieves the list of all Review objects associated with a Place.

    Args:
        place_id (str): The ID of the Place.

    Returns:
        JSON: A list of Review objects associated with the specified Place.
    """
    obj_place = storage.get(Place, place_id)
    if not obj_place:
        abort(404)
    return jsonify([obj.to_dict() for obj in obj_place.reviews])


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def single_review(review_id):
    """
    Retrieves details of a specific Review object.

    Args:
        review_id (str): The ID of the Review.

    Returns:
        JSON: Details of the specified Review object.
    """
    obj = storage.get(Review, review_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_review(review_id):
    """
    Deletes a specific Review object.

    Args:
        review_id (str): The ID of the Review.

    Returns:
        JSON: An empty dictionary with the status code 200.
    """
    obj = storage.get(Review, review_id)
    if not obj:
        abort(404)
    obj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def push_review(place_id):
    """
    Creates a new Review associated with a Place.

    Args:
        place_id (str): The ID of the Place.

    Returns:
        JSON: Details of the new Review with the status code 201.
    """
    obj_place = storage.get(Place, place_id)
    if not obj_place:
        abort(404)

    new_review = request.get_json()
    if not new_review:
        abort(400, "Invalid JSON format")
    if 'user_id' not in new_review:
        abort(400, "Missing 'user_id' attribute")
    user_id = new_review['user_id']
    obj_user = storage.get(User, user_id)
    if not obj_user:
        abort(404)
    if 'text' not in new_review:
        abort(400, "Missing 'text' attribute")

    # Create a new Review instance
    obj = Review(**new_review)
    setattr(obj, 'place_id', place_id)

    # Add the new Review to the storage
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/reviews/<review_id>',
                 methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """
    Updates details of a specific Review object.

    Args:
        review_id (str): The ID of the Review.

    Returns:
        JSON: Details of the updated Review object with the status code 200.
    """
    obj = storage.get(Review, review_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Invalid JSON format")

    # Update Review attributes based on the request
    for k, v in req.items():
        if k not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(obj, k, v)

    # Save the changes to storage
    storage.save()
    
    return make_response(jsonify(obj.to_dict()), 200)
