from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hora_actual():
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        "mensaje": "Microservicio de hora funcionando correctamente",
        "hora_actual": hora
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
