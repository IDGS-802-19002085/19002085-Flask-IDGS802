
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/operaciones', methods=["GET"])
def operacion():
    return render_template("interfaz3.html")

@app.route('/resultado', methods=["POST"])
def resultados():
    persona=request.form.get('txtNombre')
    boleta=12
    cantidad=request.form.get('CBoletas')
    cantidad=int(cantidad)
    cantidad=request.form.get('CBoletas')
    cantidad=int(cantidad)

    cantPersonas=request.form.get('CCompradores')
    cantPersonas=int(cantPersonas)

    total=int(boleta)*int(cantidad)
    more=false

    if(cantidad / cantPersonas>7):
        more=True

    if (cantidad > 5) : 
        desc= total*0.15
        pago=total-desc
        masD=(pago*0.10)
        TD=masD-pago
    elif cantidad >=3 and cantidad<=5 :
        desc= total*0.10
        pago=total-desc
        
    elif cantidad<=2:
        total=boleta*cantidad

    suma = compradores * (boletas * 12000)
    total = suma - (suma * descuento)

    return {
    'limite': more,
    'nombre': persona,
    'total': total
    }



if __name__ == '__main__':
    app.run(debug=True, port=8000)



