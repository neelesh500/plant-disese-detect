# AgriNet AI - Smart Plant Disease Detection & Agricultural Super-Platform

[![Vercel Deployment Ready](https://img.shields.io/badge/Vercel-Deployment%20Ready-000000?style=for-the-badge&logo=vercel)](https://vercel.com)
[![Python Flask](https://img.shields.io/badge/Backend-Flask%20%2F%20Python-3776AB?style=for-the-badge&logo=python)](https://flask.palletsprojects.com/)
[![ONNX Runtime](https://img.shields.io/badge/Inference-ONNX%20Runtime-005CED?style=for-the-badge)](https://onnxruntime.ai/)
[![Gemini AI](https://img.shields.io/badge/Conversational%20AI-Google%20Gemini-4285F4?style=for-the-badge&logo=google)](https://deepmind.google/technologies/gemini/)

**Developers:** Pratham Yadav, Narendra Choudhary, Neelesh Tewari, Prerak Goswami

---

## 🌟 Overview & Key Features

AgriNet AI has evolved into an **all-in-one Smart Farming Super-Portal** featuring 8 dedicated agricultural tools:

1. **🌿 AI Leaf Doctor & Disease Scanner:**
   - Detects **38 distinct crop-disease combinations** from the PlantVillage dataset using deep learning (ONNX / MobileNetV2).
   - **Detailed Pathology Brief**: Causal organisms, visual symptoms, and disease development dynamics.
   - **Certified Chemical Medicines**: Specific commercial brand names (e.g., *Dithane M-45*, *Ridomil Gold*, *Score 250 EC*, *Blitox 50*), active chemical molecules, exact dosages (e.g. `2.5 g / Liter water`), and spray intervals.
   - **Organic & Biological Solutions**: *Trichoderma viride*, *Cold-pressed Neem Oil 10,000 PPM*, and *Fermented Sour Buttermilk*.
   - **Multimodal Environmental Context**: Real-time severity tuning based on ambient temperature, humidity, and soil moisture.
   - **Quick 1-Click Demo Samples**: Test tomato early blight, potato late blight, apple scab, and healthy corn with a single click without having to download or upload images!
   - **Text-to-Speech (TTS) & Print Report**: Listen to prescriptions out loud or print an official agricultural prescription slip.

2. **🧪 Smart Fertilizer & NPK Dosage Calculator:**
   - Computes exact commercial bags of **Urea (46% N)**, **DAP (18:46:0)**, and **MOP (60% K₂O)** for 11+ crops.
   - Supports land area calculations in **Acres, Hectares, and Bigha**.
   - Provides split application timetables (Basal sowing dose vs. Top-dressing during tillering/flowering).

3. **🌾 Mandi Market Bhav & Price Trends:**
   - Real-time modal prices (₹/Quintal) across major agricultural trading hubs.
   - 24-hour trends (+/- %), min-max price ranges, and smart farmer trade signals (Sell Now vs. Hold).

4. **🐛 Crop Pest & Weed Directory:**
   - Field identification for major agricultural pests (Aphids, Whiteflies, Fall Armyworm, Spider Mites, Fruit Borers) and noxious weeds (*Parthenium*, *Cyperus rotundus*).
   - Economic injury thresholds, approved insecticides/herbicides, and biological biocontrol agents.

5. **🌱 Organic Bio-Lab (Desi Kheti Formulations):**
   - Step-by-step master preparation guides for **Jeevamrut**, **Neemastra**, **Agniastra**, and **Fermented Sour Buttermilk (Khatti Chhachh)**.

6. **🌦️ Seasonal Crop Calendar & Sowing Planner:**
   - Comprehensive schedules for **Kharif (Monsoon)**, **Rabi (Winter)**, and **Zaid (Summer)** seasons.

7. **🩺 Soil Health & pH Amendment Advisor:**
   - Interactive pH scale and texture evaluator providing targeted soil amendments (Agricultural Lime, Dolomite, Gypsum, Sulfur, Green Manuring).

8. **📜 Diagnosis History & Records:**
   - Local browser archive storing recent diagnoses, confidence scores, and prescriptions.

9. **🤖 Conversational AI Agronomy Assistant:**
   - Natural, friendly voice & text chat supporting English and Hindi/Hinglish.
   - Dual-engine architecture: uses **Google Gemini** when configured, and automatically falls back to the **Built-in Agronomy Knowledge Engine** when offline or if API key is not configured (guaranteeing zero 503 error messages!).
   - Executes UI actions (e.g., *"open camera"*, *"upload image"*, *"check fertilizer"*, *"mandi bhav"*, *"analyze"*).

---

## 🚀 Quick Setup & Local Execution

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment (Optional for Gemini)
```bash
cp .env.example .env
```
In `.env`:
```env
GEMINI_API_KEY=AIzaSyYourActualKeyHere
GEMINI_MODEL=gemini-2.5-flash
```
*(Note: If `GEMINI_API_KEY` is not set, AgriNet AI automatically uses its built-in offline agronomy intelligence without any errors!)*

### 3. Run the Flask Server
```bash
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## ☁️ Vercel Deployment Instructions

AgriNet is fully configured for deployment on Vercel:

1. **Push your code to GitHub / GitLab**.
2. **Import the repository into Vercel**.
3. **Environment Variables on Vercel (Optional)**:
   - Go to **Project Settings** -> **Environment Variables**.
   - Add `GEMINI_API_KEY` and `GEMINI_MODEL`.
4. Deploy! Vercel will build `@vercel/python` using `app.py` and serve static assets seamlessly as defined in `vercel.json`.
