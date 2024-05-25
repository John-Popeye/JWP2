from time import sleep
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task

@app.route('/')
def index():
    posts = Task.query.all()
    return render_template('index.html', posts=posts)

@app.route('/save', methods=['POST'])
def add_user():
    if request.method == 'POST':
        description = request.json['description']
        creator = request.json['creator']
        dueDate = request.json['dueDate']
        print(request.json)
        new_post = Task()
        new_post.dueDate = dueDate
        new_post.creator = creator
        new_post.description = description
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return "ok"

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        id = request.json['id']
        task = Task.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('index'))
    return "deleted"


