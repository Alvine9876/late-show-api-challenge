from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ..models.episode import Episode
from ..app import db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()

    return jsonify({"message": "Episode deleted"}), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    from ..models.episode import Episode
    from ..models.appearance import Appearance
    from ..models.guest import Guest

    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": [
            {
                "guest": appearance.guest.name,
                "rating": appearance.rating
            } for appearance in episode.appearances
        ]
    }), 200



@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {
            "id": ep.id,
            "date": ep.date.isoformat(),
            "number": ep.number
        } for ep in episodes
    ]), 200
