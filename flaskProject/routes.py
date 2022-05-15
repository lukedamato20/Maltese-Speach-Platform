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
