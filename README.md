# Plant Disease Detection Web Application

## Quick Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

Then update `.env`:

```env
GEMINI_API_KEY=your_real_key_here
GEMINI_MODEL=gemini-2.5-flash
```

Run the server:

```bash
python app.py
```
**Pratham Yadav, Narendra Choudhary, Neelesh Tewari, Prerak Goswami**

---

## 1. Introduction
The agricultural sector faces significant challenges due to crop diseases, which lead to substantial yield losses and pose a threat to global food security. The existence of an automated computational system for the detection and diagnosis of plant diseases provides valuable assistance to experts who visually inspect infected plants.

This project implements a Convolutional Neural Network (CNN) focused on plant disease detection and diagnosis using leaf images. We utilize deep learning models (such as MobileNetV2 / ResNet50) trained on the public PlantVillage dataset to classify images into 38 different plant-disease combinations.

## 2. Dataset
This model is built to be trained on the **PlantVillage Dataset**, which consists of over 50,000 augmented images across 38 distinct classes of crop-disease combinations.

## 3. Technology Stack
1. **Python & Flask:** For the backend API and serving the web interface.
2. **TensorFlow & Keras:** For Deep Learning Model architecture and inference.
3. **HTML/CSS/JS:** Vanilla web interface implementation with modern UI aesthetics (Glassmorphism, 3D tilt effects, Voice commands).

## 4. Methodology
The backend integrates a Pre-trained CNN model.
When a user uploads a leaf image, the image is passed to the Flask backend where it is pre-processed (resizing to 224x224 and tensor normalization). The deep learning model (\models/plant_disease_model.h5\) runs inference and returns the class index with the highest confidence. The application then returns the predicted disease name, confidence score, inference latency, and recommended treatment protocols.

## 5. Recent Enhancements:
- **Backend Refactoring:** Removed mock data predictions and successfully integrated real image input pre-processing for TensorFlow model inference.
- **Unified Architecture:** Simplified the tech stack by removing unused frameworks and focusing entirely on an established Python+TensorFlow pipeline.
- **Agentic AI Interface:** Frontend now includes realistic Voice-to-Text inference triggers for hands-free interactions.

## 6. Training (How to Train)
To train the model from scratch, you can use the \	rain.py\ script:
\\ash
python train.py
\*(Ensure you have downloaded the PlantVillage dataset locally and updated the dataset paths in the script before training).*

## 7. Future Scope
Immediate next steps include collecting more data to improve accuracy across a wider variety of field conditions, testing against images with multiple ailments, and deploying the trained robust \.h5\ model to a cloud endpoint.
