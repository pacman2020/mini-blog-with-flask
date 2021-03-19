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
    dados['photo'] = name_img.filename
    form = PublicationForm(**dados)

    if request.method == 'POST' and form.validate():
        
        new_publication = PublicationModel(
            title=form.title.data,
            photo=form.photo.data,
            description=form.description.data)
        new_publication.save_publication()
        return redirect('/')
    return render_template('publications/create-publication.html', form=form)