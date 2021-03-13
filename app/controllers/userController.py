from app import app, request, render_template, redirect
from app.models.User import UserModel

@app.route('/')
def list_user():
    return render_template('index.html')

@app.route('/new')
def create_user():
    if request.method == 'POST':
        pass
    return render_template('create-user.html')

@app.route('/<int:id>')
def detail_user(id):
    return 'detail user', 200


@app.route('/update/<int:id>')
def update_user(id):
    if request.method == 'POST':
        pass
    return render_template('update-user.html'), 200

@app.route('/delete/<int:id>')
def delete_user(id):
    return 'delet user', 200