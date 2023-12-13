import os
from lib.peeps_repo import PeepRepository, Peep
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect
from datetime import datetime

app = Flask(__name__)



# ///// GET Routes ////
@app.route('/', methods=['GET', 'POST'])
def get_index():

    connection = get_flask_database_connection(app)
    repo = PeepRepository(connection)

    if request.method == 'POST':
        content = request.form['content']
        #time_posted = request.form['time_posted']
        time_posted = "2023-11-01 15:25:43"

        peep = Peep(None, content, time_posted, None)
        repo.create(peep)
        peeps = repo.all()

        return redirect('/')
    else:
        peeps = repo.all()

        return render_template('index.html', peeps=peeps)

@app.route('/sign_up')
def get_sign_up():
    return render_template('sign_up.html')

@app.route('/make_post')
def get_make_post():
    return render_template('make_post.html')







if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))