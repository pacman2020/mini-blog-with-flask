from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER
from app import (
    app, 
    request, 
    render_template, 
    redirect, 
    os)
from app.models.Publication import PublicationModel
from app.forms import PublicationForm


#cria login pega usuario logado par user_id
#privatiza rotas
#paginação
#filtro de busca
#delete e update publicação

@app.route('/')
def home():
    publications = PublicationModel.query.all()
    return render_template('publications/list-publication.html', publications=publications)

@app.route('/new-publication', methods=['GET', 'POST'])
def create_publication():
    
    form = PublicationForm()
    
    if request.method == 'POST':
        #getting files file
        #taking form data and turning it into dictionaries
        file = request.files['photo']
        data = request.form.to_dict() 
        data['photo'] = file.filename

        #validated form fields
        form = PublicationForm(**data)        
        if form.validate():
            
            new_publication = PublicationModel(
                title=form.title.data,
                photo=form.photo.data,
                description=form.description.data)
            
            #path and name of the file to be saved
            #saving file in the uploads directory 
            save_path = os.path.join(
                UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(save_path)
            
            #logged in user
            new_publication.user_id = 1
            
            new_publication.save_publication()
            return redirect('/')
    return render_template('publications/create-publication.html', form=form)

@app.route('/<int:id>')
def detail_publication(id):
    publication = PublicationModel.find_by_publication(id=id)
    if publication:
        return render_template('publications/detail-publication.html', publication=publication)
    return redirect('/')