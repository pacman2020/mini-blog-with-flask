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
    name_img = request.files.get('photo')
    dados = request.form.to_dict() #pegando dados formulario
    dados['photo'] = name_img.filename #pegando image
    
    form = PublicationForm(**dados)

    if request.method == 'POST' and form.validate():
        print('<<<---->>>', form.data )
        return 'salve'
    return render_template('publications/create-publication.html', form=form)