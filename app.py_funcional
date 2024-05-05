from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def frase_random():
    try:
        # URL de la API Quotable para obtener citas aleatorias
        response = requests.get("https://api.quotable.io/random", timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Devuelve la cita y el autor
            return jsonify({'frase': data['content'], 'autor': data['author']})
        else:
            # Muestra la página de error con el código de estado HTTP
            return render_template('error.html', error_code=response.status_code)
    except requests.exceptions.RequestException as e:
        # Esto captura cualquier tipo de error en la solicitud (timeout, DNS error, etc.)
        return render_template('error.html', error_code=404)

if __name__ == '__main__':
    app.run(debug=True)

