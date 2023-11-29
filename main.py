from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def inicio():

    if request.method == 'POST':
        valor = request.form['valor']
        if valor == "1":
            return redirect(url_for('ejercicio1'))

        if valor == "2":
            return redirect(url_for('ejercicio2'))

    return render_template("index.html")


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidadTarros = int(request.form['cantidadTarros'])

        sinDescuento = cantidadTarros * 9000
        if edad < 18:
            descuento = 0
        elif (edad >= 18 and edad <= 30):
            descuento = cantidadTarros * 9000 * .15
        elif edad > 30:
            descuento = cantidadTarros * 9000 * .25

        totalPagar = sinDescuento - descuento

        return render_template("ejercicio1.html", descuento=descuento, nombre=nombre, sinDescuento=sinDescuento, totalPagar=totalPagar)

    return render_template("ejercicio1.html")


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        passw = request.form['passw']

        if nombre.lower() == "pepe" and passw == "user":
            verificar = True
        elif nombre.lower() == "juan" and passw == "admin":
            verificar = True
        else:
            verificar = False

        return render_template("ejercicio2.html", verificar=verificar, nombre=nombre)

    return render_template("ejercicio2.html")


if __name__ == '__main__':
    app.run(debug=True)
