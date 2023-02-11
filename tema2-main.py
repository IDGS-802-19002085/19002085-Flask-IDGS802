from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'soy un mensaje'

@app.route('/jimena')
def jimena():
  return '<h1>jimena</h1>'

if __name__ == '__main__':
  app.run(debug=True, port=8000)
