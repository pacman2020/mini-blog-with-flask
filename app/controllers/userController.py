from app import app, request, render_template, redirect
from app.models.User import UserModel
from app.forms import UserForm

@app.route('/')
def list_user():
    return render_template('index.html')

@app.route('/new-user',  methods=['GET', 'POST'])
def create_user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        print('--->',form.username.data,'<---')
        return 'save'
    return render_template('create-user.html', form=form)

@app.route('/<int:id>')
def detail_user(id):
    return render_template('detail-user.html')


@app.route('/update/<int:id>')
def update_user(id):
    if request.method == 'POST':
        pass
    return render_template('update-user.html'), 200

@app.route('/delete/<int:id>')
def delete_user(id):
    return 'delet user', 200