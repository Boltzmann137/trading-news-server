from flask import Flask, send_file
import datetime

app = Flask(__name__)

# Archivo con datos de análisis de mercado
NEWS_FILE = "news_analysis.txt"

@app.route('/news_analysis.txt')
def get_news_file():
    """Sirve el archivo de análisis de noticias."""
    return send_file(NEWS_FILE, as_attachment=True)

@app.route('/update_news', methods=['POST'])
def update_news():
    """Actualiza el archivo con información nueva."""
    with open(NEWS_FILE, "w") as file:
        file.write(f"AAPL: 0.9\nMSFT: 0.6\nGOOGL: -0.4\nAMZN: 0.1\nActualizado en: {datetime.datetime.now()}\n")
    return "Archivo actualizado correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
