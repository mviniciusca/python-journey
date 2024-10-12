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

    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        imc = imc_ref.imc(weight, height)
    else:
        error = 'Invalid Values'
    return render_template('imc.html', methods=["GET", "POST"],error=error, imc=imc)

if __name__ == '__main__':
    app.run(debug=True)