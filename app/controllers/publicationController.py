from werkzeug.utils import secure_filename
from flask import request, redirect, render_template, url_for
from config import UPLOAD_FOLDER
import os
from app import app
from app.models.Publication import PublicationModel
from app.forms import PublicationForm
from flask_login import current_user, login_required


@app.route('/')
def list_publication():
    search = request.args.get('search')
    #paginação
    page = request.args.get('page')
    
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    
    if search:
        publications = PublicationModel.query.filter_by(
            title=search).paginate(page=page, per_page=2)
    else:
        publications = PublicationModel.query.order_by(
            PublicationModel.id.desc()).paginate(page=page, per_page=2)
    
    return render_template(
        'publications/list-publication.html', publications=publications)
    
@app.route('/new', methods=['GET', 'POST'])
@login_required
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
            new_publication.user_id = current_user.id
            
            new_publication.save_publication()
            return redirect(url_for('list_publication'))
    return render_template('publications/create-publication.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_publication(id):
    
    publication = PublicationModel.find_by_publication(id)
    form = PublicationForm(obj=publication)
    
    if request.method == 'POST' and publication.user_id == current_user.id:
        
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

@app.route('/<int:id>')
def detail_publication(id):
    publication = PublicationModel.find_by_publication(id=id)
    if publication:
        return render_template('publications/detail-publication.html', publication=publication)
    return redirect(url_for('list_publication'))

@app.route('/delete/<int:id>')
@login_required
def delete_publication(id):
    publication = PublicationModel.query.get(id)
    if publication and publication.user_id == current_user.id :
        publication.delete_publication()
        return  redirect(url_for('list_publication'))
    return redirect(url_for('list_publication'))
