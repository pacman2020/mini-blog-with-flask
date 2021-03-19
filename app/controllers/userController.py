from app import app, request, render_template, redirect
from app.models.User import UserModel
from app.forms import UserForm, UserFormUpdate

@app.route('/list-user')
def list_user():
    users = UserModel.query.all()
    return render_template('users/list-user.html',users=users)

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
    return render_template('users/create-user.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    form = UserFormUpdate(request.form)
    user = UserModel.find_by_user(id)
    
    if request.method == 'POST' and form.validate():
        user.username=form.username.data
        user.save_user()
        return redirect('/list-user')
    return render_template('users/update-user.html', form=form, user=user )

@app.route('/delete/<int:id>')
def delete_user(id):
    user = UserModel.find_by_user(id)
    error = 'usuario nao encontrado!'
    if user:
        try:
            user.delete_user()
            return redirect('/list-user')
        except:
            error = 'erro ao deletar usuario'
            return redirect('/list-user', error=error )
    return redirect('/list-user', error=error )