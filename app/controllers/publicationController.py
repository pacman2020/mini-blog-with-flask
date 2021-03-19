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

@app.route('/new-publication', methods=['GET', 'POST'])
def create_publication():
    data = request.form.to_dict() #pegando dados formulario
    data['photo'] = request.files #pegando image
    
    form = PublicationForm(**data)

    if request.method == 'POST' and form.validate():
        print('<<<---->>>', form.data)
        return 'salve'
    return render_template('publications/create-publication.html', form=form)