from app import(
    app, 
    request, 
    render_template, 
    redirect, 
    url_for,
    login_required,
    login_user,
    logout_user
    )
from app.models.User import UserModel
from app.forms import UserForm, UserFormUpdate, LoginForm

#cria login
#cria login pega usuario logado pra user_id
#privatiza rotas


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserModel.find_email(form.email.data)
        
        if user.check_hash(request.form['password']) and user:
            
            #guardando na session
            login_user(user)
            return redirect(url_for('list_publication'))
            
    return render_template('users/login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/user')
@login_required
def list_user():
    users = UserModel.query.all()
    return render_template('users/list-user.html',users=users)

@app.route('/user/new',  methods=['GET', 'POST'])
def create_user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = UserModel(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data)
        
        new_user.hash_password()
        new_user.save_user()
        return redirect(url_for('list_user'))
    return render_template('users/create-user.html', form=form)

@app.route('/user/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    form = UserFormUpdate(request.form)
    user = UserModel.find_by_user(id)
    
    # print('---->', session['username'] )
    # if  'username' in session:
        
    if request.method == 'POST' and form.validate():
        user.username=form.username.data
        user.save_user()
        return redirect(url_for('list_user'))
    return render_template('users/update-user.html', form=form, user=user )
    # return redirect(url_for('list_user'))

@app.route('/user/delete/<int:id>')
def delete_user(id):
    user = UserModel.find_by_user(id)
    error = 'usuario nao encontrado!'
    if user:
        user.delete_user()
        return redirect(url_for('list_user'))
    return redirect('/list-user', error=error )

