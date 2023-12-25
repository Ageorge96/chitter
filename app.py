import os
from lib.peeps_repo import PeepRepository, Peep
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect
from datetime import datetime

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def get_index():

    connection = get_flask_database_connection(app)
    repo = PeepRepository(connection)

    
    peeps = repo.all(True)

    return render_template('index.html', peeps=peeps)
    
    

@app.route('/sign_up')
def get_sign_up():
    return render_template('sign_up.html')

@app.route('/make_post', methods=['GET', 'POST'])
def get_make_post():

    connection = get_flask_database_connection(app)
    repo = PeepRepository(connection)

    if request.method == 'POST':
        content = request.form['content']

        peep = Peep(None, content, datetime.now(), None)
        repo.create(peep)

        return redirect('/')
    else:
        return render_template('make_post.html')




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))