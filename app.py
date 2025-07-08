from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Threat description map (optional, expand as needed)
threat_descriptions = {
    'SOFTWARE': 'Related to software or system tools.',
    'attack-pattern': 'Known attacker tactic or technique.',
    'benign': 'Appears safe, no threat detected.',
    'identity': 'Mentions credentials or identities.',
    'location': 'Geographic/physical info potentially linked to threats.',
    'malware': 'Malicious payload or software detected.',
    'threat-actor': 'Linked to a known attacker/group.',
    'vulnerability': 'Describes a known system weakness.',
    # Add more as needed
}

# Initialize Flask app
app = Flask(__name__)

# Load model and preprocessing assets
model = tf.keras.models.load_model("cyber_threat_model.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No input text provided.'}), 400

    # Preprocess input
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=200)

    # Predict
    preds = model.predict(padded)
    predicted_index = np.argmax(preds)
    predicted_class = label_encoder.inverse_transform([predicted_index])[0]
    confidence = float(np.max(preds))

    return jsonify({
        'prediction': predicted_class,
        'confidence': f"{confidence * 100:.2f}%",
        'description': threat_descriptions.get(predicted_class, 'No description available.')
    })

if __name__ == '__main__':
    app.run(debug=True)
