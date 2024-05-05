from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

def get_profile_image_url(author_slug, size=200):
    """Genera la URL para la imagen de perfil del autor."""
    IMAGE_BASE = 'https://images.quotable.dev/profile'
    return f"{IMAGE_BASE}/{size}/{author_slug}.jpg"

@app.route('/')
def frase_random():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Extrae el slug del autor para generar la URL de la imagen
            author_slug = data['authorSlug']
            image_url = get_profile_image_url(author_slug)
            return jsonify({
                'frase': data['content'],
                'autor': data['author'],
                'imagen': image_url
            })
        else:
            return render_template('error.html', error_code=response.status_code)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_code=404)

if __name__ == '__main__':
    app.run(debug=True)

