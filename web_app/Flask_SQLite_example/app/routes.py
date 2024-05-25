from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Teacher, User

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if username and email:
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete_user.html')



@app.route('/add-teacher', methods=['POST','GET'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        time = request.form['time']
        if name and subject and time:
            new_Teacher = Teacher(name=name, subject=subject, time=time)
            db.session.add(new_Teacher)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_teacher.html')

@app.route('/delete-teacher', methods=['POST','GET'])
def delete_teacher():
    if request.method == 'POST':
        teacher_id = request.form['id']
        teacher = Teacher.query.get(id)
        if teacher:
            db.session.delete(teacher)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete_teacher.html')