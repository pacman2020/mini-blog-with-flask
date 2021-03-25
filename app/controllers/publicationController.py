from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER
from app import (
    app, 
    request, 
    render_template, 
    redirect, url_for,
    os)
from app.models.Publication import PublicationModel
from app.forms import PublicationForm


#privatiza rotas
#paginação
#cria login pega usuario logado pra user_id
#criptografa senha
#deletar usuario deletar tudo sore ele
#filtro de busca
#update publicação

@app.route('/publication/')
def list_publication():
    publications = PublicationModel.query.all()
    return render_template('publications/list-publication.html', publications=publications)

@app.route('/publication/new', methods=['GET', 'POST'])
def create_publication():
    
    form = PublicationForm()
    
    if request.method == 'POST':
        #getting files file
        #taking form data and turning it into dictionaries
        file = request.files['photo']
        data = request.form.to_dict() 
        data['photo'] = file

        #validated form fields
        form = PublicationForm(**data)
        if form.validate():
            
            new_publication = PublicationModel(
                title=form.title.data,
                photo=file.filename,
                description=form.description.data)
            
            #path and name of the file to be saved
            #saving file in the uploads directory 
            save_path = os.path.join(
                UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(save_path)
            
            #logged in user
            new_publication.user_id = 1 #usuario temporario ate criar login
            
            new_publication.save_publication()
            return redirect(url_for('list_publication'))
    return render_template('publications/create-publication.html', form=form)


@app.route('/publication/update/<int:id>', methods=['GET', 'POST'])
def update_publication(id):
    
    publication = PublicationModel.find_by_publication(id)
    #print(publication.photo)
    #publication['photo'] = 'save_path' #colocar arquivo
    form = PublicationForm(obj=publication)

    return render_template(
        'publications/update-publication.html', 
        form=form, publication=publication)


@app.route('/publication/<int:id>')
def detail_publication(id):
    publication = PublicationModel.find_by_publication(id=id)
    if publication:
        return render_template('publications/detail-publication.html', publication=publication)
    return redirect(url_for('list_publication'))

@app.route('/publication/delete/<int:id>')
def delete_publication(id):
    publication = PublicationModel.query.get(id)
    if publication:
        publication.delete_publication()
        return  redirect(url_for('list_publication'))
    return redirect(url_for('list_publication'))
