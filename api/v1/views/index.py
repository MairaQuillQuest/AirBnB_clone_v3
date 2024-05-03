#!/usr/bin/python3
"""
Module index:
   url_prefix = '/api/v1'
   routes:
       - '/status'
       - '/stats'
"""

from flask import jsonify
from models import storage
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats')
def stats():
    """Retrieve the number of each object by type"""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
