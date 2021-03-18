from app import app, request, render_template, redirect
from app.models.Publication import PublicationModel


@app.route('/')
def home():
    publications = [
        {'title':'saasas',
         'description':'aasdada'
        }
    ]
    return render_template('publications/list-publication.html', publications=publications)