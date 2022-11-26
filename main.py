from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')

if __name__ == 'main':
    app.run(debug=True)