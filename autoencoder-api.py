from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS  # <-- importar CORS

app = Flask(__name__)        # <-- crear app Flask
CORS(app)                    # <-- habilitar CORS

# Carga tus pesos guardados (por ejemplo, en un archivo .npz)
# Aquí solo ejemplo dummy
def load_model():
    # Simula pesos
    weights = np.array([1.0, 2.0, 3.0])
    return weights

weights = load_model()

def predict(x):
    # Tu lógica de autoencoder con numpy
    # Ejemplo dummy: producto punto con pesos
    x = np.array(x)
    pred = np.dot(x, weights)
    return pred.tolist()

@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.json
    x = data.get('input')
    result = predict(x)
    return jsonify({'prediction': result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)