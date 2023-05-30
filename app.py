from flask import request, jsonify, render_template

from fake_data import generate_fake_data
from user import *


@app.route('/user', methods=['POST'])
def create_user():  # Створює нового користувача з вказаним ім'ям та електронною поштою і зберігає його в базі даних.
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.id)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):  # Отримує і повертає інформацію про користувача на основі наданого ідентифікатора користувача.
    user = User.query.get(user_id)
    if user is None:
        return 'User not found', 404
    return jsonify({'name': user.name, 'email': user.email})


@app.route('/')
def home():  # Збирає всіх користувачів і відображає їх на головній сторінці за допомогою шаблону.
    users = User.query.all()
    return render_template('home.html', users=users)


if __name__ == "__main__":
    with app.app_context():
        if User.query.count() == 0:  # Генерує користувачів тільки при умові відсутності їх у бд
            generate_fake_data(100)
    generate_fake_data(100)
    app.run()
