from flask import Blueprint, jsonify
from ..models.guest import Guest

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()

    return jsonify([
        {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        }
        for guest in guests
    ]), 200
