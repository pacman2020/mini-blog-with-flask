from app import app, request, render_template, redirect
from app.models.User import UserModel
from app.forms import UserForm

@app.route('/list-user')
def list_user():
    users = UserModel.query.all()
    return render_template('list-user.html',users=users)

@app.route('/new-user',  methods=['GET', 'POST'])
def create_user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = UserModel(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data)
        new_user.save_user()
        return redirect('/list-user')
    return render_template('create-user.html', form=form)

@app.route('/update/<int:id>')
def update_user(id):
    if request.method == 'POST':
        pass
    return render_template('update-user.html'), 200

@app.route('/delete/<int:id>')
def delete_user(id):
    return 'delet user', 200