from app import app, request, render_template, redirect
from app.models.Publication import PublicationModel
from app.forms import PublicationForm

@app.route('/')
def home():
    publications = [
        {'title':'saasas',
         'description':'aasdada'
        }
    ]
    return render_template('publications/list-publication.html', publications=publications)

@app.route('/create-publication')
def create_publication():
    form = PublicationForm()
    if request.method == 'POST' and form.validate():
        return 'salve'
    return render_template('publications/create-publication.html', form=form)