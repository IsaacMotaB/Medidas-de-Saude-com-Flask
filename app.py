from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/imc/<p>/')
def imc(p, h):
  p = float(p)
  h = float(p)
  imc_ = p / (h*h)
  return render_template('hello.html', imc=imc_)

@app.route('/')
@app.route('/<user>')
def index(user=None):
  return render_template('hello.html', name=user)


app.run(host='0.0.0.0', port=81)
