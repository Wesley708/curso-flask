from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        peso = request.form['pesoForm']
        altura = request.form['alturaForm']
        if peso == '':
            peso = 0
        if altura == '':
            altura = 0
        if peso == 0 and altura == 0:
            return render_template('index.html', resultado = 'Sem IMC')
        else:
            resultado = peso / (altura * altura)
            return render_template('index.html', resultado = resultado)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)