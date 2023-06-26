from flask import Flask, render_template, request, redirect, url_for
from database import create_student, get_students, get_student_by_id, update_student_result

app = Flask(_name_)

@app.route('/')
def index():
    students = get_students()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        marks = request.form['marks']
        create_student(name, marks)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = get_student_by_id(student_id)
    if request.method == 'POST':
        marks = request.form['marks']
        update_student_result(student_id, marks)
        return redirect(url_for('index'))
    return render_template('edit.html', student=student)

if _name_ == '_main_':
    app.run(debug=True)