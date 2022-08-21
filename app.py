from contextlib import redirect_stderr
from flask import Flask, render_template, flash, url_for, redirect
from config import Config
from nanoid import generate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Config) 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#from modal import Links #db Store --> import here to prevent circular imports
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    res = False
    var = None
    #dup = None
    short_link = None
    form= InputForm()
    if form.validate_on_submit():
        var = form.long_url.data
        if form.alias.data:
            alias = form.alias.data
        else:
            alias = generate(size=5)
        data = Links(user_link =form.long_url.data, alias = alias )
        db.session.add(data)
        db.session.commit()
        short_link = 'https://tinybits.herokuapp.com/'+alias 
        form.long_url.data = ''
        res = True

    return render_template('index.html', res = res, var = var, form=form, short_link=short_link)
@app.route('/<path:link_id>')
def fetch_link(link_id):
    long_url = Links.query.filter_by(alias=link_id).first()
    if long_url:
        return redirect(long_url.user_link) 
from inputForms import InputForm
from modal import Links

