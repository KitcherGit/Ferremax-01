from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import os
import binascii

app = Flask(__name__)

# Context proccesors 

@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

# Endpoints

# Secret Key

# Generar una clave secreta aleatoria
clave_secreta = binascii.hexlify(os.urandom(24)).decode()


# Asignar la clave secreta a la aplicación Flask
app.secret_key = clave_secreta

# End Secret Key


#Aqui empieza el LOGIN

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Verificar la autenticación (omitido por simplicidad)

        # Si la autenticación es exitosa, almacenar el email en la sesión
        session['email'] = email
        session['cart'] = []  # Inicializar un carrito de compras vacío
        return render_template('productos.html')  # Redirigir a la página de productos
    return render_template('login.html')

#Aqui termina el LOGIN

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)