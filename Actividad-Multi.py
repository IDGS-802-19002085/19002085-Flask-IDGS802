from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/operasSuma', methods=["GET"])
def operasbas():
    return render_template("operasbas.html")

@app.route('/resultado', methods=["POST"])
def resultado():
    n1=request.form.get('txtNum1')
    n2=request.form.get('txtNum2')  
    i=-1
    while (n1 == 0):
        n2=n2
        print(n2)
    return render_template("resultado.html", n2=n2)
        
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)

