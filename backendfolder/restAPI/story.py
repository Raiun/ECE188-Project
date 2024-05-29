from flask_restful import Resource, reqparse
from models import Story
from database import db

story_parser = reqparse.RequestParser()
story_parser.add_argument('title', type=str, required=True, help='Title of the story is required')
story_parser.add_argument('content', type=str, required=True, help='Content of the story is required')
story_parser.add_argument('author', type=str, required=True, help='Author of the story is required')

class StoryResource(Resource):
    def get(self, story_id):
        story = Story.query.get_or_404(story_id)
        return {'id': story.id, 'title': story.title, 'content': story.content, 'author': story.author}

    def delete(self, story_id):
        story = Story.query.get_or_404(story_id)
        db.session.delete(story)
        db.session.commit()
        return {'message': 'Story deleted'}

    def put(self, story_id):
        story = Story.query.get_or_404(story_id)
        args = story_parser.parse_args()
        story.title = args['title']
        story.content = args['content']
        story.author = args['author']
        db.session.commit()
        return {'message': 'Story updated', 'story': {'id': story.id, 'title': story.title, 'content': story.content, 'author': story.author}}

class StoryListResource(Resource):
    def get(self):
        stories = Story.query.all()
        return [{'id': story.id, 'title': story.title, 'content': story.content, 'author': story.author} for story in stories]

    def post(self):
        args = story_parser.parse_args()
        story = Story(title=args['title'], content=args['content'], author=args['author'])
        db.session.add(story)
        db.session.commit()
        return {'message': 'Story created', 'story': {'id': story.id, 'title': story.title, 'content': story.content, 'author': story.author}}, 201
