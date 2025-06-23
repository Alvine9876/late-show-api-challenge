from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models.appearance import Appearance
from ..models.guest import Guest
from ..models.episode import Episode
from ..app import db

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")

    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return jsonify({"error": "Guest or episode not found"}), 404

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        "id": appearance.id,
        "guest": guest.name,
        "episode": episode.number,
        "rating": appearance.rating
    }), 201
