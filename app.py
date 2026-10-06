import random
import time

from flask import Flask, jsonify, render_template, request

# To fully run the model, you'd integrate TensorFlow or PyTorch here.
# import tensorflow as tf
# from hybrid_model import HybridEnsembleModel
import logging
import os
import numpy as np
from PIL import Image
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

model = None
# Allowed extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        logger.warning("Predict endpoint hit with no file uploaded.")
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        logger.warning("Predict endpoint hit with empty filename.")
        return jsonify({"error": "No file selected"}), 400

    try:
        if file and allowed_file(file.filename):
            logger.info(f"Processing uploaded file: {file.filename}")
            
            # Start timer for actual latency measurement
            start_time = time.time()
            
            # Extract Multimodal Environmental Inputs
            temperature = float(request.form.get("temperature", 25.0))
            humidity = float(request.form.get("humidity", 60.0))
            soil_moisture = float(request.form.get("soil_moisture", 40.0))
            
            logger.info(f"Received Environmental Data -> Temp: {temperature}C, Humidity: {humidity}%, Moisture: {soil_moisture}%")

            # Try loading the model dynamically if not loaded
            # Note: For production, it's better to load the model globally, but for this mini-project, 
            # loading it globally or caching it is good.
            global model
            if model is None:
                # Prioritize ONNX for smaller deployment size (e.g., Vercel)
                if os.path.exists("models/plant_disease_model.onnx"):
                    try:
                        import onnxruntime as ort
                        model = ort.InferenceSession("models/plant_disease_model.onnx")
                        logger.info("Loaded models/plant_disease_model.onnx successfully using ONNX Runtime.")
                    except Exception as e:
                        logger.error(f"Error loading ONNX model: {e}")
                elif os.path.exists("models/plant_disease_model.h5"):
                    try:
                        import tensorflow as tf
                        model = tf.keras.models.load_model("models/plant_disease_model.h5")
                        logger.info("Loaded models/plant_disease_model.h5 successfully using TensorFlow.")
                    except Exception as e:
                        logger.error(f"Error loading h5 model: {e}")
                
            # Process the image
            image = Image.open(file.stream).convert('RGB')
            image = image.resize((224, 224))
            img_array = np.array(image) / 255.0  # Normalize to [0, 1]
            img_array = np.expand_dims(img_array, axis=0) # Shape: (1, 224, 224, 3)
            
            # Diseases List (Subset of PlantVillage for Mapping)
            PLANT_DISEASES = [
                ('Apple - Apple Scab', 'Apply zinc-based fungicide during blooming.'),
                ('Apple - Black Rot', 'Prune infected branches and apply fungicide.'),
                ('Apple - Cedar Apple Rust', 'Remove nearby cedar trees and use fungicides.'),
                ('Apple - Healthy', 'No treatment required. Maintain overall plant health.'),
                ('Blueberry - Healthy', 'No treatment required. Maintain overall plant health.'),
                ('Cherry - Powdery Mildew', 'Apply sulfur or potassium bicarbonate.'),
                ('Cherry - Healthy', 'No treatment required.'),
                ('Corn - Gray leaf spot', 'Use resistant varieties; apply fungicide if severe.'),
                ('Corn - Common rust', 'Apply fungicide when rust first appears.'),
                ('Corn - Northern Leaf Blight', 'Plant resistant hybrids. Apply agricultural fungicides if lesions appear early in the season.'),
                ('Corn - Healthy', 'No treatment required.'),
                ('Grape - Black Rot', 'Apply fungicides properly timed.'),
                ('Grape - Esca', 'Remove infected wood and apply wound protectants.'),
                ('Grape - Leaf blight', 'Apply fungicides during the rainy season.'),
                ('Grape - Healthy', 'No treatment required.'),
                ('Orange - Citrus greening', 'Remove infected trees and control psyllid vectors.'),
                ('Peach - Bacterial spot', 'Plant resistant varieties and maintain tree health.'),
                ('Peach - Healthy', 'No treatment required.'),
                ('Pepper, bell - Bacterial spot', 'Use copper-based sprays and pathogen-free seed.'),
                ('Pepper, bell - Healthy', 'No treatment required.'),
                ('Potato - Early blight', 'Use copper-based fungicides. Remove infected leaves.'),
                ('Potato - Late blight', 'Use chlorothalonil. Avoid overhead irrigation and ensure good soil drainage.'),
                ('Potato - Healthy', 'No treatment required.'),
                ('Raspberry - Healthy', 'No treatment required.'),
                ('Soybean - healthy', 'No treatment required.'),
                ('Squash - Powdery mildew', 'Apply sulfur products and ensure good air circulation.'),
                ('Strawberry - Leaf blight', 'Remove infected leaves from plants.'),
                ('Strawberry - Healthy', 'No treatment required.'),
                ('Tomato - Bacterial spot', 'Use copper fungicidal sprays.'),
                ('Tomato - Early blight', 'Apply copper-based fungicides. Remove infected leaves to prevent spore spread.'),
                ('Tomato - Late blight', 'Apply chlorothalonil. Avoid overhead watering.'),
                ('Tomato - Leaf Mold', 'Increase air circulation and use fungicides.'),
                ('Tomato - Septoria leaf spot', 'Remove infected lower leaves and use fungicide.'),
                ('Tomato - Spider mites', 'Use horticultural oils or insecticidal soaps.'),
                ('Tomato - Target Spot', 'Use appropriate fungicides.'),
                ('Tomato - Tomato Yellow Leaf Curl Virus', 'Control whiteflies using insecticides or reflective mulches.'),
                ('Tomato - Tomato mosaic virus', 'Use resistant varieties and remove infected plants.'),
                ('Tomato - Healthy', 'No treatment required.')
            ]
            
            # Predict using the Model
            if model is not None:
                try:
                    # Check if the model is ONNX or Keras
                    if hasattr(model, 'run'): # ONNX InferenceSession
                        img_array_f32 = img_array.astype(np.float32)
                        input_name = model.get_inputs()[0].name
                        preds = model.run(None, {input_name: img_array_f32})[0]
                    else: # TensorFlow/Keras
                        preds = model.predict(img_array)
                        
                    class_idx = np.argmax(preds[0])
                    confidence = preds[0][class_idx] * 100
                    
                    # Try to load real class names if trained
                    class_names = []
                    if os.path.exists("models/class_names.json"):
                        with open("models/class_names.json", "r") as f:
                            class_names = json.load(f)
                    
                    if class_names and class_idx < len(class_names):
                        disease_name = class_names[class_idx]
                        
                        # Find matching treatment
                        treatment = "No specific protocol found. Maintain general plant health."
                        for d_mapping, t_mapping in PLANT_DISEASES:
                            if d_mapping.lower() in disease_name.lower().replace("_", " ") or disease_name.lower().replace("_", " ") in d_mapping.lower():
                                treatment = t_mapping
                                break
                    else:
                        if class_idx < len(PLANT_DISEASES):
                            disease_name, treatment = PLANT_DISEASES[class_idx]
                        else:
                            disease_name, treatment = "Unknown Anomaly", "No protocol found."
                            
                except Exception as e:
                    logger.error(f"Error during prediction: {e}")
                    return jsonify({"error": "Inference Engine Error"}), 500
            else:
                return jsonify({"error": "Model not loaded. Please train or deploy the model correctly."}), 500
            
            # Calculate severity based on AI confidence and Envrionmental Factors (Rule-based Multimodal Agronomy Engine)
            # This makes the environmental inputs functional and biologically logical
            if "healthy" in disease_name.lower():
                severity = 0.0
            else:
                # Base severity inversely proportional to confidence (lower confidence = higher spread variability)
                base_sev = max(10.0, 100 - confidence) 
                
                # Environmental multipliers (Fungal/Bacterial diseases spread faster in high humidity and moisture)
                env_multiplier = 1.0
                if humidity > 70.0: env_multiplier += 0.2
                if temperature > 28.0 and temperature < 35.0: env_multiplier += 0.15 
                
                severity = min(100.0, base_sev * env_multiplier)

            # Calculate actual processing latency
            latency_ms = int((time.time() - start_time) * 1000)

            response = {
                "disease": disease_name.replace("_", " ").title(),
                "treatment": treatment,
                "confidence": f"{confidence:.2f}",
                "latency": f"{latency_ms}",
                "severity_percentage": f"{severity:.1f}"
            }

            return jsonify(response)

        return jsonify({"error": "Invalid file type"}), 400
    except Exception as e:
        logger.error(f"Error in prediction pipeline: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("🌿 AgriNet AI - Deep Learning Server Started")
    print("Serving on http://127.0.0.1:5000")
    # In production, do not use debug=True
    app.run(debug=True, port=5000)
