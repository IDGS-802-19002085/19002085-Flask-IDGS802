from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def index():
  titulo='Hola'
  lista=['Pedro', 'laura', 'Luis', 'mensaje']
  return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/Alumnos')
def alumnos():
    return render_template("alumnos.html")
@app.route('/Usuarios')
def usuarios():
    return render_template("usuarios.html")



if __name__ == '__main__':
  app.run(debug=True, port=8000)