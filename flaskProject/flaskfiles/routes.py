from flaskfiles import app
from flask import Flask, redirect, url_for, render_template, request


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
    text = request.form['text']
    text_manipulation(text)

    return redirect('demo.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 404