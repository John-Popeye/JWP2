from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), unique=False, nullable=False)
    dueDate = db.Column(db.String(200), unique=False, nullable=False)
    creator = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
