from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:abc@127.0.0.1:5432/postgres"
db = SQLAlchemy(app)
api = Api(app)
# DATABASE_URL = "postgresql+psycopg2://postgres:abc@127.0.0.1:5432/postgres" old: 'sqlite:///database.db'

class UserModel(db.Model):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    gamesWon = db.Column(db.Integer, default=0)
    gamesPlayed = db.Column(db.Integer, default=0)
    gamesAbandoned = db.Column(db.Integer, default=0)
    rating = db.Column(db.Integer, default=100) #WIP
    creationDate = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User(id = {self.id}, password = {self.password}, gamesWon = {self.gamesWon}, gamesPlayed = {self.gamesPlayed}, rating = {self.rating})"

user_args = reqparse.RequestParser()
user_args.add_argument('id', type=str, required=True, help="UserId cannot be blank")
user_args.add_argument('password', type=str, required=True, help="Password cannot be blank")

userFields = {
    'id':fields.String,
    'password':fields.String,
    'gamesWon':fields.Integer,
    'gamesPlayed':fields.Integer,
    'gamesAbandoned':fields.Integer,
    'rating':fields.Integer,
    'creationDate':fields.DateTime
}

class Users(Resource):
    #Get a list of all the players information
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    #Create a player
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(id=args["id"], password=args["password"])
        db.session.add(user)
        db.session.commit()
        #users = UserModel.query.all()
        return user, 201
    

class User(Resource):
    #Get a specific player
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user
    
    #Change password
    @marshal_with(userFields)
    def post(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        user.password = args["password"]
        db.session.commit()
        return user
    
    #Update stats after game played
    @marshal_with(userFields)
    def patch(self, id):
        user = UserModel.query.filter_by(id=id).first()
        user.gamesPlayed = user.gamesPlayed + 1
        db.session.commit()
        return user

    #Delete player
    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 204

api.add_resource(Users, '/player/')
api.add_resource(User, '/player/<string:id>')

@app.route("/")
def home():
    return "<h1>Truf</h1>"

if __name__ == '__main__':
    app.run(debug=True)