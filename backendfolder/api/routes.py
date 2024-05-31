from flask import Blueprint, request, jsonify
from models import db, User, Story, Evaluation
import random

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@main.route('/stories', methods=['POST'])
def create_story():
    data = request.get_json()
    new_story = Story(title=data['title'], content=data['content'])
    db.session.add(new_story)
    db.session.commit()
    return jsonify({"message": "Story created"}), 201

@main.route('/evaluations', methods=['POST'])
def create_evaluation():
    data = request.get_json()
    new_evaluation = Evaluation(score=data['score'], user_id=data['user_id'], story_id=data['story_id'])
    db.session.add(new_evaluation)
    db.session.commit()
    return jsonify({"message": "Evaluation created"}), 201

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"username": user.username, "email": user.email, "evaluations": [{"score": e.score, "story_id": e.story_id} for e in user.evaluations]})

@main.route('/stories/<int:story_id>', methods=['GET'])
def get_story(story_id):
    story = Story.query.get_or_404(story_id)
    return jsonify({"title": story.title, "content": story.content})

@main.route('/recommendations', methods=['GET'])
def get_recommendations():
    stories = Story.query.all()
    if not stories:
        return jsonify({"message": "No stories available"}), 404

    recommended_stories = random.sample(stories, min(len(stories), 3))

    recommendations = [{"id": story.id, "title": story.title, "content": story.content} for story in recommended_stories]
    return jsonify({"recommendations": recommendations})
