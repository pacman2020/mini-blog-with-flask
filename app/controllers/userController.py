from app import app


@app.route('/')
def list_user():
    return 'home', 200

@app.route('/new')
def create_user():
    return 'create user', 201

@app.route('/<int:id>')
def detail_user(id):
    return 'detail user', 200


@app.route('/update/<int:id>')
def update_user(id):
    return 'update user', 200

@app.route('/delete/<int:id>')
def delete_user(id):
    return 'delet user', 200