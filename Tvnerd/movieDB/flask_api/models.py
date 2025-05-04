from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'TVnerd_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Movie(db.Model):
    __tablename__ = 'TVnerd_movie'
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    poster_path = db.Column(db.String(255))
    overview = db.Column(db.Text)
    is_featured = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

class Notification(db.Model):
    __tablename__ = 'TVnerd_notification'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('TVnerd_user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    related_movie_id = db.Column(db.Integer, db.ForeignKey('TVnerd_movie.id'), nullable=True)
    user = db.relationship('User', backref='notifications')
    related_movie = db.relationship('Movie', backref='notifications')

    def __repr__(self):
        return f'<Notification for {self.user_id}: {self.message}>'