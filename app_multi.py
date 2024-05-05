from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

def get_profile_image_url(author_slug, size=200):
    """Genera la URL para la imagen de perfil del autor."""
    IMAGE_BASE = 'https://images.quotable.dev/profile'
    return f"{IMAGE_BASE}/{size}/{author_slug}.jpg"

def translate_text(text, src_lang='en', dest_lang='es'):
    """Traduce texto del inglés al español utilizando LibreTranslate."""
    url = "https://libretranslate.com/translate"
    params = {
        "q": text,
        "source": src_lang,
        "target": dest_lang,
        "format": "text"
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(url, json=params, headers=headers)
    if response.status_code == 200:
        return response.json()['translatedText']
    else:
        return "Error en la traducción"

@app.route('/')
def frase_random():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=10)
        if response.status_code == 200:
            data = response.json()
            author_slug = data['authorSlug']
            image_url = get_profile_image_url(author_slug)
            translated_text = translate_text(data['content'])
            return render_template('quote.html', frase=data['content'], autor=data['author'], imagen=image_url, traduccion=translated_text)
        else:
            return render_template('error.html', error_code=response.status_code)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_code=404)

if __name__ == '__main__':
    app.run(debug=True)

