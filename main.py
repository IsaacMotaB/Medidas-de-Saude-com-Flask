from flask import Flask, request
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/imc')
def imc():
  p = (request.values.get('peso'))
  h = (request.values.get('altura'))
  imc_ = p and h \
    and float(p) / float(h)**2
  return render_template('imc.html', imc=imc_)

@app.route('/agua')
def agua():
  p = (request.values.get('peso'))
  consumo = p and float(p) * 35
  return render_template('agua.html', agua=consumo)

@app.route('/circ')
def circuferencia():
  risco = None
  circum = request.values.get('circum')
  sexo = request.values.get('sexo')
  if circum:
    circum = float(circum)
    if sexo == 'feminino':
      if circum <= 80:  
        risco = 'normal'
      elif circum < 84:
        risco = 'médio'
      elif circum < 88:
        risco = 'alto'
      else:
        risco = 'altíssimo'
    elif sexo == 'masculino':
      if circum <= 90:  
        risco = 'normal'
      elif circum < 94:
        risco = 'médio'
      elif circum < 102:
        risco = 'alto'
      else:
        risco = 'altíssimo'
  return render_template('circ.html', risco=risco)

@app.route('/')
def index(user=None):
  return render_template('index.html', name=user)



app.run(host='0.0.0.0', port=81)