from flask import Flask

app = Flask(__name__)

@app.route('/oi')
def index():
    return 'Hello, World isso!'

if __name__ == '__main__':
    app.run(debug=True)