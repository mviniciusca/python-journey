from flask import Flask
from flask import render_template
from flask import request
from imc import imc_ref

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('hello.html')
@app.route('/app', methods=["GET", "POST"])
def imc():
    error = None
    height = None
    weight = None
    imc = None

    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        if weight <= 0 or height <= 0:
            error = 'Erro: Digite um valor maior que zero.'
        else:
            imc = imc_ref.imc(weight, height)
    else:
        error = 'Erro: Digite um valor válido!'
    return render_template('imc.html', methods=["GET", "POST"],error=error, imc=imc, height=height, weight=weight)

if __name__ == '__main__':
    app.run(debug=True)