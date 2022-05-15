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
    

# @app.route('/testing_flask/result', methods=['POST', "GET"])
# def testing_flask_demo():
#     output = request.form.to_dict()
#     name = output["name"]
#     return render_template('testing_flask.html',name=name,title='TTS - Demo',)