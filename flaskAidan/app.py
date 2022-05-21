from ttsdemo import *

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def testing_flask():
    return render_template('testing_flask.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    text_manipulation(text)

    return redirect('/play_audio/')

@app.route('/play_audio/')
def playaudio():
    return render_template('playaudio.html')
    
# @app.route('/home')
# def home():
#     return render_template('testing_flask.html')

# @app.route('/home')
# def home():
#     return render_template('index.html', title='TTS - Home')


# @app.route('/about')
# @app.route('/about/')
# def about():
#     return render_template('about.html', title='TTS - About')


# @app.errorhandler(404)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html'), 404


# @app.errorhandler(500)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('500.html'), 404

# @app.route('/testing_flask/result', methods=['POST', "GET"])
# def testing_flask_demo():
#     output = request.form.to_dict()
#     name = output["name"]
#     return render_template('testing_flask.html',name=name,title='TTS - Demo',)