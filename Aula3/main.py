from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    dados = {
        'nome' : 'Wesley',
        'sobrenome' : 'Alves',
        'idade' : 27
    }
    return render_template('index.html', dados = dados)

@app.route('/filtros')
def filtros():
    return render_template('filtros.html',valor = 3.43434)

@app.route('/imagem')
def imagem():
    return render_template('imagem.html')

@app.route('/idade/<int:idade>')
def idade(idade):
    return render_template('ifelse.html', idade = idade)

@app.route('/frutas')
def frutas():
    frutas = ['Laranja', 'Maça', 'Uva', 'Pera', 'Abacaxi']
    return render_template('for.html', frutas = frutas)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nomeForm']
        email = request.form['emailForm']
        print(f"Nome : {nome}")
        print(f"Email : {email}")
        return render_template('formulario.html', nome = nome, email = email)
    else:
        return render_template('formulario.html')
    
@app.route('/contato')
def contato():
    return render_template('link/contato.html')

@app.route('/home')
def home():
    return render_template('link/home.html') 

if __name__ == '__main__':
    app.run(debug=True)