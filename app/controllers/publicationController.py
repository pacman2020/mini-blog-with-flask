from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER
from app import (
    app, 
    request, 
    render_template, 
    redirect, url_for,
    session,
    os)
from app.models.Publication import PublicationModel
from app.forms import PublicationForm



#paginação
#deletar usuario deletar tudo sore ele
#filtro de busca

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
    form = PublicationForm(obj=publication)
    
    if request.method == 'POST':
        
        file = request.files['photo']
        data = request.form.to_dict() 
        
        if file:
            data['photo'] = file
            form = PublicationForm(**data)
            if form.validate():
                publication.title = form.title.data
                publication.description = form.description.data
                publication.photo = file.filename
                #path and name of the file to be saved
                #saving file in the uploads directory 
                save_path = os.path.join(
                    UPLOAD_FOLDER, secure_filename(file.filename))
                file.save(save_path)
                
                #logged in user
                # publication.user_id = 1 #usuario temporario ate criar login
                
                publication.save_publication()
                return redirect(url_for('list_publication'))
        
        data['photo'] = publication.photo
        form = PublicationForm(**data)
        if form.validate():
            publication.title = form.title.data
            publication.description = form.description.data
            # print('--->', publication)
            
            publication.save_publication()
            return redirect(url_for('list_publication'))

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
