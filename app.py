from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return {"mensaje": "Microservicio de hora funcionando correctamente"}

@app.route('/hora')
def hora():
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"hora_actual": ahora}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
