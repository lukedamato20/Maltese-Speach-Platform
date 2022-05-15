from flaskfiles import app
from flask import render_template, request


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='TTS - Home')


@app.route('/about')
@app.route('/about/')
def about():
    return render_template('about.html', title='TTS - About')


@app.route('/demo')
@app.route('/demo/')
def demo():
    return render_template('demo.html', title='TTS - Demo')


@app.route('/demo/result', methods=['POST', "GET"])
def demo_result():
    output = request.form.to_dict()
    name = output["name"]
    return render_template('demo.html',name=name,title='TTS - Demo',)
