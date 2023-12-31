import os
from lib.peeps_repo import PeepRepository, Peep
from lib.userdata_repo import UserdataRepository
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect, session
from datetime import datetime
from lib.operations import *

app = Flask(__name__)

def get_repos():
    connection = get_flask_database_connection(app)
    return PeepRepository(connection), UserdataRepository(connection)

@app.route('/', methods=['GET', 'POST'])
def get_index():

    peep_repo, user_repo = get_repos()

    
    peeps = peep_repo.all(True)

    return render_template('index.html', peeps=peeps)
    
    

@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    #https://www.youtube.com/watch?v=3NEzo3CfbPg
    
    #Priority: https://www.youtube.com/watch?v=71EU8gnZqZQ

    peep_repo, user_repo = get_repos()

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = pass_to_hash(request.form["password"])
        
        user_repo.new_user(username, email, password)

        return redirect("/")

    else:
        return render_template('sign_up.html')
    

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/make_post', methods=['GET', 'POST'])
def get_make_post():

    connection = get_flask_database_connection(app)
    peep_repo = PeepRepository(connection)

    if request.method == 'POST':
        content = request.form['content']

        peep = Peep(None, content, datetime.now(), None)
        peep_repo.create(peep)

        return redirect('/')
    else:
        return render_template('make_post.html')




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))