from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

NEWS_FILE = "news_analysis.txt"

@app.route('/')
def home():
    return jsonify({"message": "Servidor funcionando. Usa /news_analysis.txt para obtener el archivo de noticias."})

@app.route('/news_analysis.txt')
def get_news_file():
    """Sirve el archivo de análisis de noticias."""
    if os.path.exists(NEWS_FILE):
        return send_file(NEWS_FILE, as_attachment=True)
    return "Archivo no encontrado", 404

@app.route('/update_news', methods=['POST'])
def update_news():
    """Actualiza el archivo con información nueva."""
    with open(NEWS_FILE, "w") as file:
        file.write("AAPL: 0.9\nMSFT: 0.6\nGOOGL: -0.4\nAMZN: 0.1\nEl mercado muestra señales alcistas.\n")
    return "Archivo actualizado correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
