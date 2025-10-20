from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/hora', methods=['GET'])
def obtener_hora():
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"hora_actual": hora_actual})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
