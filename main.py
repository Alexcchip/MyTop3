from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/list')
def list():
    pass

if __name__ == 'main':
    app.run(debug=True)