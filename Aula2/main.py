from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World isso!'

@app.route('/canal')
def canal():
    return 'Esse é o meu canal'

@app.route('/ola/<nome>/<int:idade>')
def ola(nome, idade):
    nome = escape(nome)
    idade = escape(idade)
    return f'<h1 style="color:blue">Olá {nome}, você tem {idade} anos</h1>'

if __name__ == '__main__':
    app.run(debug=True)