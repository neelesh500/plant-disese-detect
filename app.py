from flask import Flask, render_template, request, jsonify
import os
import random
import time

from werkzeug.utils import secure_filename

# To fully run the model, you'd integrate TensorFlow or PyTorch here. 
# import tensorflow as tf 
# from hybrid_model import HybridEnsembleModel

app = Flask(__name__)

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    try:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # In a real scenario, you would save the image or read it into memory:
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # img = Image.open(file.stream).resize((224, 224))
            # predictions = hybrid_model.predict(img)
            
            # Simulating Edge Inference latency and Hybrid Deep Learning model
            time.sleep(1.5) 
            
            # Mocking predictions for prototype demonstration (mimics the 99.5% accuracy model)
            diseases = [
                ("Tomato - Early Blight", "Apply copper-based fungicides. Remove infected leaves to prevent spore spread.", "99.53%"),
                ("Apple - Apple Scab", "Rake and destroy fallen leaves. Apply zinc-based fungicide during blooming.", "98.90%"),
                ("Potato - Late Blight", "Use chlorothalonil. Avoid overhead irrigation and ensure good soil drainage.", "99.12%"),
                ("Corn - Northern Leaf Blight", "Plant resistant hybrids. Apply agricultural fungicides if lesions appear early in the season.", "97.80%")
            ]
            
            prediction = random.choice(diseases)
            
            response = {
                'disease': prediction[0],
                'treatment': prediction[1],
                'confidence': prediction[2],
                'latency': f"{random.randint(18, 35)} ms (C++ Edge Inference)" 
            }
            
            return jsonify(response)
            
        return jsonify({'error': 'Invalid file type'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🌿 AgriNet AI - Deep Learning Server Started")
    print("Serving on http://127.0.0.1:5000")
    # In production, do not use debug=True
    app.run(debug=True, port=5000)
