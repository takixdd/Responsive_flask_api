from flask import Flask
from flask import render_template
from flask import send_from_directory


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    key = ''  # My api key
    return render_template('home.html', api_key=key)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/kontakt')
def kontakt_page():
    return render_template('informacje.html')


@app.route('/Cennik')
def cennik_page():
    return render_template('cennik.html')


@app.route('/galeria')
def galeria_page():
    return render_template('galeria.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'static/favicon.ico', mimetype='image/vnd.microsoft.icon')



if __name__ == '__main__':
    app.run(debug=True)